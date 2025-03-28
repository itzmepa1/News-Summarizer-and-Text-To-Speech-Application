import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS
import os
import json
import spacy
import torch
from newspaper import Article  
from transformers import pipeline 
from deep_translator import GoogleTranslator
# Load spaCy model for topic extraction
nlp = spacy.load("en_core_web_sm")

# Check for GPU support
device = 0 if torch.cuda.is_available() else -1

# Load summarization model with GPU acceleration
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=device)


def generate_summary(text):
    """Generate a concise summary using a Transformer-based model."""
    if not text.strip():
        return "No summary available."

    try:
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
        return summary[0]["summary_text"]
    
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "Summary could not be generated."


def extract_topics(text):
    """Extract key topics using Named Entity Recognition (NER) and return a proper list."""
    doc = nlp(text)
    topics = sorted(set(ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "GPE", "EVENT"]))
    return topics if topics else ["General"]


def analyze_sentiment(text):
    """Perform sentiment analysis and classify as Positive, Negative, or Neutral."""
    sentiment = TextBlob(text).sentiment.polarity
    return "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"


def fetch_news(company_name):
    """Fetches news articles using BeautifulSoup (bs4) to ensure non-JS content."""
    search_url = f"https://www.bing.com/news/search?q={company_name}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for item in soup.find_all("a", class_="title")[:15]:  # Fetch more and filter down to 10
        title = item.text.strip()
        link = item["href"]

        try:
            article = Article(link)
            article.download()
            article.parse()
            content = article.text[:1500]  # Limit text for better summarization
        except Exception:
            content = "Summary not available."

        summary = generate_summary(content)
        topics = extract_topics(summary)

        articles.append({
            "Title": title,
            "Summary": summary,
            "Sentiment": analyze_sentiment(summary),
            "Topics": topics
        })

        if len(articles) >= 10:  # Stop at 10 unique articles
            break

    return {"Company": company_name, "Articles": articles} if articles else {"error": f"No news found for {company_name}."}


def comparative_analysis(articles):
    """Generates comparative sentiment analysis and topic overlap."""
    sentiment_distribution = {"Positive": 0, "Negative": 0, "Neutral": 0}
    topic_sets = [set(article["Topics"]) for article in articles if article["Topics"]]

    # Compute sentiment distribution
    for article in articles:
        sentiment_distribution[article["Sentiment"]] += 1

    # Ensure Common Topics are correctly extracted
    if len(topic_sets) > 1:
        common_topics = sorted(set.intersection(*topic_sets))  # Find shared topics across all articles
    else:
        common_topics = []  # If only one article, no common topics exist

    # Format Unique Topics Properly
    unique_topics = {
        f"Unique Topics in Article {i+1}": sorted(list(topic_sets[i] - set(common_topics)))
        for i in range(len(topic_sets))
    }

    # Compare coverage differences properly
    coverage_differences = [
        {
            "Comparison": f"Article {i+1} discusses {articles[i]['Title']}, while Article {i+2} covers {articles[i+1]['Title']}.",
            "Impact": f"One focuses on {', '.join(articles[i]['Topics'])}, while the other highlights {', '.join(articles[i+1]['Topics'])}."
        }
        for i in range(len(articles) - 1)
    ]

    return {
        "Sentiment Distribution": sentiment_distribution,
        "Coverage Differences": coverage_differences,
        "Topic Overlap": {
            **unique_topics
        }
    }


def generate_final_sentiment_summary(analysis, company_name):
    """Creates a final sentiment summary based on article sentiment analysis."""
    total_articles = sum(analysis["Sentiment Distribution"].values())
    if total_articles == 0:
        return "No significant trend detected."

    positive_ratio = analysis["Sentiment Distribution"]["Positive"] / total_articles
    negative_ratio = analysis["Sentiment Distribution"]["Negative"] / total_articles

    if positive_ratio > 0.6:
        return f"{company_name} is receiving mostly positive coverage, suggesting strong investor confidence."
    elif negative_ratio > 0.6:
        return f"Recent news around {company_name} is mostly negative, indicating potential challenges."
    else:
        return f"News coverage for {company_name} is mixed, with both positive and negative aspects."


def text_to_speech(text, filename="static/output.mp3"):
    """Convert the final sentiment analysis into Hindi speech using gTTS."""
    os.makedirs("static", exist_ok=True)
    filepath = os.path.join("static", filename)

    try:
        # Translate English to Hindi
        hindi_text = GoogleTranslator(source='auto', target='hi').translate(text)
        if not hindi_text.strip():
            raise ValueError("Translated text is empty!")

        print(f"🔹 Hindi Text: {hindi_text}")  # Debugging log

        # Generate speech
        tts = gTTS(text=hindi_text, lang="hi", slow=False)
        tts.save(filepath)

        # Verify if the file is actually created
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Audio file not created at {filepath}")

        print(f"Audio generated successfully: {filepath}")
        return filepath

    except Exception as e:
        print(f"Error generating speech: {e}")
        return None

def process_news(company_name):
    """Fetches, processes news, performs sentiment analysis, and generates Hindi TTS."""
    news_data = fetch_news(company_name)
    if "error" in news_data:
        return news_data

    articles = news_data.get("Articles", [])
    analysis = comparative_analysis(articles)
    final_summary = generate_final_sentiment_summary(analysis, company_name)

    final_output = {
        "Company": company_name,
        "Articles": articles,
        "Comparative Sentiment Score": analysis,
        "Final Sentiment Analysis": final_summary
    }

    # Generate Hindi TTS for the sentiment summary
    speech_file = text_to_speech(final_summary)
    final_output["Audio"] = speech_file if speech_file else "Error generating audio"

    return final_output

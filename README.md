# News-Summarizer-and-Text-To-Speech-Application
# 📰 News Summarization & Sentiment Analysis with Hindi TTS  
### 🚀 Multi-Article Summarization, Sentiment Analysis, and Hindi Speech Synthesis  

![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%94-red)  
![FastAPI](https://img.shields.io/badge/FastAPI-%E2%9C%94-blue)  
![Hugging Face](https://img.shields.io/badge/HuggingFace-%E2%9C%94-yellow)  
![Python](https://img.shields.io/badge/Python-3.8+-blue)  
![TTS](https://img.shields.io/badge/Text--to--Speech-Hindi-green)  

## 📌 Project Overview  
This project extracts, summarizes, and analyzes **news articles** related to a given **company** and generates a **Hindi text-to-speech (TTS)** summary of the sentiment report.  

🔹 **News Extraction** – Fetches at least **10 unique articles** using **BeautifulSoup (bs4)**.  
🔹 **Summarization** – Uses **Hugging Face Transformers** for concise summaries.  
🔹 **Sentiment Analysis** – Classifies news as **Positive, Negative, or Neutral** using **TextBlob**.  
🔹 **Topic Extraction** – Uses **spaCy NER** to extract **key topics**.  
🔹 **Comparative Analysis** – Compares **news trends, sentiment, and topic overlaps**.  
🔹 **Hindi TTS** – Converts the final sentiment summary into **playable Hindi audio**.  

✅ **Tech Stack:** Python, Streamlit, FastAPI, BeautifulSoup, Hugging Face Transformers, gTTS, TextBlob, spaCy, Deep-Translator  

---

## ⚡ Features
✔ Fetches the latest company news (from non-JS sources).  
✔ Summarizes news content using a Transformer-based model.  
✔ Performs sentiment analysis on each article.  
✔ Extracts key topics to highlight coverage.  
✔ Generates a comparative analysis of news trends.  
✔ Converts summary to Hindi speech for easy listening.  

---

## 📂 Project Structure
\`\`\`
📂 News-Summarization-TTS
├── 📜 app.py           # Streamlit Web UI
├── 📜 api.py           # FastAPI Backend
├── 📜 utils.py         # Core Processing Functions
├── 📜 requirements.txt # Required Dependencies
├── 📜 README.md        # Project Documentation
└── 📂 static/          # Folder for Audio Storage
\`\`\`

---

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
\`\`\`bash
git clone https://github.com/yourusername/News-Summarization-TTS.git
cd News-Summarization-TTS
\`\`\`

### 2️⃣ Create a Virtual Environment (Optional)
\`\`\`bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
\`\`\`

### 3️⃣ Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4️⃣ Download Required NLP Models
\`\`\`bash
python -m spacy download en_core_web_sm
\`\`\`

---

## 🚀 Running the Application
### 1️⃣ Start the FastAPI Backend
\`\`\`bash
uvicorn api:app --reload
\`\`\`
📌 Visit API Docs: \`http://127.0.0.1:8000/docs\`

### 2️⃣ Run the Streamlit Web App
\`\`\`bash
streamlit run app.py
\`\`\`
📌 Visit Web App: \`http://localhost:8501\`

---

## 📌 API Endpoints
| Method | Endpoint | Description |
|--------|---------|------------|
| \`GET\`  | \`/analyze/{company_name}\` | Fetches and analyzes news about a company. |

---

## 🎙️ Example Output (JSON)
\`\`\`json
{
    "Company": "Tesla",
    "Articles": [
        {
            "Title": "Tesla's New Model Breaks Sales Records",
            "Summary": "Tesla's latest EV sees record sales in Q3...",
            "Sentiment": "Positive",
            "Topics": ["Electric Vehicles", "Stock Market", "Innovation"]
        }
    ],
    "Comparative Sentiment Score": {
        "Sentiment Distribution": {
            "Positive": 1,
            "Negative": 0,
            "Neutral": 0
        },
        "Topic Overlap": {
            "Common Topics": ["Electric Vehicles"],
            "Unique Topics in Article 1": ["Stock Market", "Innovation"]
        }
    },
    "Final Sentiment Analysis": "Tesla has received mostly positive media coverage.",
    "Audio": "static/output.mp3"
}
\`\`\`

---

## 🛠️ Deployment
### Deploy on Hugging Face Spaces
1️⃣ **Push your code to GitHub.**  
2️⃣ **Create a new Hugging Face Space** (Streamlit template).  
3️⃣ **Upload your files and set \`requirements.txt\`.**  
4️⃣ **Run \`app.py\`** and start your application!  

---

## 📌 Contributors
👨‍💻 **Your Name** – Pavan N

📩 **Contact:** pavankumarnmv331@gmail.com 

🚀 **GitHub:** [GitHub Repository](https://github.com/yourusername/News-Summarization-TTS)  
🚀 **Hugging Face:** [Hugging Face Space](https://huggingface.co/spaces/yourspace/news-summarizer)  

---

## 📜 License
MIT License. Feel free to use, modify, and distribute! 🎯 

import streamlit as st
import json
from utils import process_news, text_to_speech
import os

def main():
    st.title("News Summarization & Sentiment Analysis")
    company = st.text_input("Enter Company Name")

    if st.button("Fetch News"):
        with st.spinner("Fetching and Analyzing News..."):
            articles = process_news(company)

            if articles and "error" not in articles:
                st.subheader("Analysis Results")
                st.json(articles)  # Display structured JSON output

                # Generate Hindi TTS for final sentiment analysis
                sentiment_report = articles.get("Final Sentiment Analysis", "No sentiment summary available.")
                speech_file = text_to_speech(sentiment_report)

                # **Play button for Hindi TTS**
                st.subheader("🎙️ Hindi Sentiment Summary (TTS)")
                
                if speech_file and os.path.exists(speech_file):
                    st.subheader("Hindi Sentiment Summary(TTS)")
                    st.audio(speech_file, format="audio/mp3")  # Play Button
                    st.download_button(
                        label="Download Hindi Audio",
                        data=open(speech_file, "rb"),
                        file_name="sentiment_summary.mp3",
                        mime="audio/mp3"
                    )
                else:
                    st.error("Audio could not be generated.")

            else:
                st.error("No articles found or an error occurred.")

if __name__ == "__main__":
    main()

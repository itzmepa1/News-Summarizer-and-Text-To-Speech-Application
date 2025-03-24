from fastapi import FastAPI
from utils import process_news
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/analyze/{company_name}")
def analyze_news(company_name: str):
    """
    API endpoint to fetch news, analyze sentiment, extract topics,
    generate comparative analysis, and return Hindi TTS for sentiment summary.
    """
    news_data = process_news(company_name)

    if "error" in news_data:
        return JSONResponse(content=news_data, status_code=404)

    return JSONResponse(content=news_data, status_code=200)

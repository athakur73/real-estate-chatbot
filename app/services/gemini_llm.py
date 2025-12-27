
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GOOGLE_API_KEY

def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0,
        google_api_key="AIzaSyAuMjjJNhr25xGUUxbECZLnqYaGaaJIsug"
    )

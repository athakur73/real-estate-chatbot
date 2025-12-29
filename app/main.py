from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.api.save import router as save_router

app = FastAPI(
    title="Agent Mira – Real Estate Chatbot",
    version="1.0.0"
)

# ✅ CORS CONFIG (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5185","http://localhost:5186", "https://frontend-real-estate-chatbot-phi.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(save_router)

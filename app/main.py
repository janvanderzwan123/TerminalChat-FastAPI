from fastapi import FastAPI
from app.seeders.seed import run_seeders
from app.api.endpoints import user, auth, chat, chat_member, message, media
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.on_event("startup")
def on_startup():
    run_seeders()
    
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(chat.router, prefix="/chats", tags=["Chats"])
app.include_router(chat_member.router, prefix="/chat-members", tags=["Chat Members"])
app.include_router(message.router, prefix="/messages", tags=["Messages"])
app.include_router(media.router, prefix="/media", tags=["Media"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

origins = [
    "http://localhost:4180",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
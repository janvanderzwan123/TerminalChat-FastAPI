from fastapi import FastAPI
from app.seeders.seed import run_seeders
from app.api.endpoints import user, auth
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.on_event("startup")
def on_startup():
    run_seeders()
    
app.include_router(auth.router, tags=["Auth"])
app.include_router(user.router, tags=["Users"])

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
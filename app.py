from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import openai
import os

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


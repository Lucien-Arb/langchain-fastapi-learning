from dotenv import load_dotenv
import os
from fastapi import FastAPI
from .database import init_db
from app import routers
from fastapi.openapi.utils import get_openapi

from langchain_core.messages import HumanMessage
from langchain_mistralai.chat_models import ChatMistralAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

app = FastAPI(
    title="FastAPI with JWT, Postgres and LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
    swagger_ui_parameters={"operationsSorter": "method"}
)

app.include_router(routers.authentication.router)
app.include_router(routers.prompt.router)
app.include_router(routers.user.router)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/mistral/{message}", tags=["MistralAI"])
async def get_mistral_ai(message: str):
    model = ChatMistralAI()
    #prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
    messages = [HumanMessage(content=message)]
    response = model.invoke(messages)
    return response

@app.get("/mistral/template/{message}", tags=["MistralAI"])
async def get_mistral_ai_with_template(message: str):
    model = ChatMistralAI()
    prompt = ChatPromptTemplate.from_template("Tell me a joke about {message}")
    chain = prompt | model
    response = chain.invoke({"message": message})
    return response
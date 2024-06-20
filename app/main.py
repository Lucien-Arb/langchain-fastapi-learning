from dotenv import load_dotenv
import os
from fastapi import FastAPI
from .database import init_db
from app import routers
from fastapi.openapi.utils import get_openapi

from langchain_core.messages import HumanMessage
from langchain_mistralai.chat_models import ChatMistralAI
from langchain.prompts import ChatPromptTemplate

#from gpt4all import GPT4All
#from langchain.llms import GPT4AllModel
#from langchain.prompts import ChatPromptTemplate

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

model = ChatMistralAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

# Initialiser le modèle GPT4All avec Mistral
#gpt4all = GPT4All(model_name="mistral-7b-openorca.Q4_0.gguf")
#model = GPT4AllModel(gpt4all=gpt4all)
#prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def read_root():
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    print(openai_api_key)
    # chat = ChatMistralAI()
    # messages = [HumanMessage(content="Quel artiste chante Bendo na bendo et ou se trouve le bendo ?")]
    # response = chat.invoke(messages)
    # print(response)
    return {"Hello": "World"}
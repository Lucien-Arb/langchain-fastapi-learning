from dotenv import load_dotenv
import os
from fastapi import FastAPI
from .database import init_db
from app import routers
from fastapi.openapi.utils import get_openapi
from langserve import add_routes
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

model = ChatMistralAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

add_routes(
    app,
    model,
    path="/chat",
)

#add_routes(
#    app,
#    prompt | model,
#    path="/generate",
#)

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
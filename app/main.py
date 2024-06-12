from dotenv import load_dotenv
import os
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
# import uvicorn
# import openai
# from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
# from langchain_core.messages import HumanMessage
# from langchain_mistralai.chat_models import ChatMistralAI


load_dotenv()
app = FastAPI()

#openai_api_key = "sk-proj-nYFaQIe0tbyzETLB25vUT3BlbkFJh6eOlaS6s9jUO5UIywez"
#prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
#model = ChatOpenAI(model="gpt-3.5-turbo")
#chain = prompt | model
#response = chain.invoke({"topic":"chicken"})
#print(response)

@app.get("/")
async def read_root():
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    print(openai_api_key)
    # chat = ChatMistralAI()
    # messages = [HumanMessage(content="Quel artiste chante Bendo na bendo et ou se trouve le bendo ?")]
    # response = chat.invoke(messages)
    # print(response)
    return {"Hello": "World"}
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

## Langchain Tracking
os.environ["LANGCHAIN_TRACING_V2"] = 'true'
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

## Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's queries"),
    ("user", "Question: {question}"),
])

## Streamlit Framework
st.title("Langchain Initial Chatbot")
input_text = st.text_input("Search the topic you want to know about")

# OpenAI LLM
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    verbose=True
)

output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
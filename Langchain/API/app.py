from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM # Ollama LLM is technically a third-party LLM

from langserve import add_routes
import uvicorn
import os

from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
app = FastAPI(
    title="Langchain Server",
    description="A simple Langchain server using Ollama LLM",
    version="0.1.0",
)

llm = OllamaLLM(
    model="gemma3",
    temperature=0,
    verbose=True
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Write a comprehensive essay about the given topic."),
    ("user", "Please write an essay about: {topic}")
])

chain = prompt | llm

# Add routes with the chain
add_routes(
    app,
    chain,
    path="/essay",  # This will create endpoints at /essay/invoke, /essay/stream, etc.
)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000
    )
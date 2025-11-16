import os

# 🔥 Disable LangSmith to fix Pydantic v2 errors on Streamlit Cloud
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_TRACING"] = "false"
os.environ["LANGCHAIN_ENDPOINT"] = ""
os.environ["LANGCHAIN_API_KEY"] = ""
os.environ["LANGCHAIN_PROJECT"] = ""

from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq

from tools.calculator_tool import calculator_tool
from tools.weather_tool import weather_tool
from tools.search_tool import search_tool
from tools.email_tool import email_tool
from tools.todo_tool import todo_tool

from config import GROQ_API_KEY


def create_agent():
    # Initialize LLM
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.3-70b-versatile"
    )

    # Register tools
    tools = [
        calculator_tool,
        weather_tool,
        search_tool,
        email_tool,
        todo_tool
    ]

    # Create LangChain Agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )

    return agent

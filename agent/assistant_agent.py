import os
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_API_KEY"] = ""

from langchain.tools import Tool
from langchain.agents import create_react_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from tools.calculator_tool import calculator_tool
from tools.weather_tool import weather_tool
from tools.search_tool import search_tool
from tools.email_tool import email_tool
from tools.todo_tool import todo_tool

from config import GROQ_API_KEY


def create_agent():
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.3-70b-versatile"
    )

    tools = [
        calculator_tool,
        weather_tool,
        search_tool,
        email_tool,
        todo_tool
    ]

    template = """You are an AI assistant. Use the tools when needed.
Follow this format:

Question: the input question
Thought: think about what to do
Action: the tool to use
Action Input: the input for the tool
Observation: tool result
... repeat ...
Final Answer: answer to the question

Begin!
Question: {input}
Thought:"""

    prompt = PromptTemplate(
        template=template,
        input_variables=["input"]
    )

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    return agent

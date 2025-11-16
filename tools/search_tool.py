import requests
from langchain.tools import tool

@tool("search")
def search_tool(query: str) -> str:
    """Search the internet via DuckDuckGo API."""
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url).json()
    return response.get("AbstractText") or "No direct answer found, but I can search again."

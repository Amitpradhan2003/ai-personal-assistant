from langchain.tools import tool

@tool("calculator")
def calculator_tool(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        return str(eval(expression))
    except:
        return "Error: invalid math expression."

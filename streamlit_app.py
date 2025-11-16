import streamlit as st
from agent.assistant_agent import create_agent

# Initialize agent only once
if "agent" not in st.session_state:
    st.session_state.agent = create_agent()

agent = st.session_state.agent

# Streamlit Page Settings
st.set_page_config(page_title="AI Personal Assistant", page_icon="🤖", layout="wide")

# Page Header
st.title("🤖 AI Personal Assistant")
st.write("Your intelligent tool-powered agent built using LangChain + Groq ✨")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# User chat input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # show user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Run the agent
    with st.spinner("Thinking..."):
        try:
            result = agent.run(user_input)
        except Exception as e:
            result = f"Error: {str(e)}"

    # show assistant message
    st.chat_message("assistant").write(result)
    st.session_state.messages.append({"role": "assistant", "content": result})

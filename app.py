import streamlit as st
import logging
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools.context_presence_judge import build_context_presence_tool
from tools.context_relevance_checker import build_context_relevance_tool
from tools.context_splitter import build_context_splitter_tool
from tools.web_search_tool import WebSearchTool

# Streamlit Cloud: secrets are stored in st.secrets
api_key = st.secrets["OPENROUTER_API_KEY"]

# Configure LLM (OpenRouter via ChatOpenAI)
llm = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=api_key,
    temperature=0.7
)

def build_agent(llm):
    tools = [
        build_context_presence_tool(llm),
        build_context_relevance_tool(llm),
        build_context_splitter_tool(llm),
        WebSearchTool
    ]
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

# Streamlit UI
st.set_page_config(page_title="LangChain Agent", page_icon="🤖", layout="centered")
st.title("🤖 LangChain Agent with OpenRouter")

# Keep chat history in session
if "messages" not in st.session_state:
    st.session_state.messages = []

agent = build_agent(llm)

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = agent.invoke(prompt)
            st.markdown(response)

    # Save response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

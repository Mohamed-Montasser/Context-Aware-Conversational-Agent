# import logging
# from langchain_ollama import OllamaLLM            # NEW import
# from langchain.agents import initialize_agent, AgentType
# from tools.context_presence_judge import build_context_presence_tool
# from tools.context_relevance_checker import build_context_relevance_tool
# from tools.context_splitter import build_context_splitter_tool
# from tools.web_search_tool import WebSearchTool
#
# try:
#     from loguru import logger
#     logger.level("AGENT", no=38, color="<yellow><bold>")
# except ImportError:
#     logger = logging.getLogger(__name__)
#
# def build_agent(llm):
#     tools = [
#         build_context_presence_tool(llm),
#         build_context_relevance_tool(llm),
#         build_context_splitter_tool(llm),
#         WebSearchTool
#     ]
#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # FIXED
#         verbose=True,
#         handle_parsing_errors=True
#     )
#     return agent
#
# if __name__ == "__main__":
#     llm = OllamaLLM(model="llama3")   # NEW class
#     agent = build_agent(llm)
#     while True:
#         user = input("Ask me anything> ")
#         logger.log("AGENT", f"User query: {user}")
#         answer = agent.invoke(user)    # .invoke preferred in new LangChain
#         print(answer)
# agent/agent_runner.py

import logging
import os
from langchain_openai import ChatOpenAI        # use ChatOpenAI wrapper
from langchain.agents import initialize_agent, AgentType
from tools.context_presence_judge import build_context_presence_tool
from tools.context_relevance_checker import build_context_relevance_tool
from tools.context_splitter import build_context_splitter_tool
from tools.web_search_tool import WebSearchTool

try:
    from loguru import logger
    logger.level("AGENT", no=38, color="<yellow><bold>")
except ImportError:
    logger = logging.getLogger(__name__)

def build_agent(llm):
    tools = [
        build_context_presence_tool(llm),
        build_context_relevance_tool(llm),
        build_context_splitter_tool(llm),
        WebSearchTool
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    return agent

if __name__ == "__main__":
    # Get OpenRouter API key from environment variable
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("Missing OPENROUTER_API_KEY environment variable")

    # Initialize LLM with OpenRouter
    llm = ChatOpenAI(
        model="openai/gpt-oss-20b:free",         # OpenRouter model
        openai_api_base="https://openrouter.ai/api/v1",  # Override base URL
        openai_api_key=api_key,
        temperature=0.7
    )

    agent = build_agent(llm)

    while True:
        user = input("Ask me anything> ")
        logger.log("AGENT", f"User query: {user}")
        answer = agent.invoke(user)
        print(answer)

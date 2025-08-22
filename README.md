# Chat with Your Context – A Context-Aware Conversational Agent

🚀 A smart, autonomous chatbot that intelligently judges, retrieves, and validates context to provide accurate and relevant answers.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://context-aware-conversational-agent.streamlit.app/)

---

## ✨ How It Works

This isn't your average chatbot. It's a **context-aware agent** that uses a large language model to reason like a human assistant. For every question, it autonomously decides to:

1.  **🕵️ Judge** if you provided enough background info.
2.  **🌐 Search** the web if context is missing.
3.  **🎯 Check** if the found information is relevant.
4.  **✂️ Split** the context from your core question.
5.  **🤖 Answer** using all the gathered information.

## 🚀 Try It Out!

The agent is live and ready to chat! Ask it anything:

*   **Direct Questions:** *"Explain quantum computing."*
*   **Questions with Context:** *"Based on the article I provided, what was the main conclusion?"*
*   **Complex Queries:** *"Compare the economic policies of country X and country Y."*

**Simply type your question into the chatbox on the live app and see how the agent reasons behind the scenes!**

## 🛠️ Project Overview

This project is built entirely on an open-source stack:

*   **Agent Framework:** [LangChain](https://www.langchain.com/) for orchestrating the agent's reasoning and tool use.
*   **LLM:** [OpenAI (via OpenRouter)](https://openrouter.ai/) powering the core intelligence (initially tested with [Ollama](https://ollama.com/) locally).
*   **Web Search:** [Tavily API](https://tavily.com/) for retrieving real-time information.
*   **Web UI & Deployment:** [Streamlit](https://streamlit.io/) for the clean interface and seamless cloud deployment.

## 📁 Project Structure

```
langchain_chat_with_context/
├── app.py                       # Main Streamlit application file
├── agent/
│   └── agent_runner.py          # Logic for initializing the LangChain agent
├── tools/                       # Directory containing the agent's tools
│   ├── context_presence_judge.py
│   ├── web_search_tool.py
│   ├── context_relevance_checker.py
│   └── context_splitter.py
├── prompts/                     # Contains all LLM prompt templates
│   ├── context_judge_prompt.txt
│   ├── relevance_checker_prompt.txt
│   └── context_splitter_prompt.txt
└── requirements.txt             # Python dependencies
```

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Note:** This project is a demonstration of advanced LLM agentic workflows using LangChain. Performance depends on the underlying LLM and API configurations.
```

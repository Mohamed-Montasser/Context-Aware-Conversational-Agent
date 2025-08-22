# import wikipedia
# from langchain.tools import Tool
#
# def wiki_search(query: str) -> str:
#     try:
#         return wikipedia.summary(query, sentences=3)
#     except Exception as e:
#         return f"No result found ({e})"
#
# WebSearchTool = Tool.from_function(
#     func=wiki_search,
#     name="WebSearchTool",
#     description="Retrieves external knowledge when context is missing"
# )
import requests
from langchain.tools import Tool
from typing import Optional
import json


class TavilySearchError(Exception):
    """Custom exception for Tavily search errors"""
    pass


def web_search(
        query: str,
        api_key: Optional[str] = None,
        max_results: int = 3
) -> str:
    """
    Perform a web search using Tavily API

    Args:
        query: Search query string
        api_key: Tavily API key (if not provided as environment variable)
        max_results: Maximum number of results to return

    Returns:
        str: Concatenated search results or error message
    """
    try:
        # Get API key from parameter or environment variable
        api_key = "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"
        if not api_key:
            raise TavilySearchError("Tavily API key not provided")

        response = requests.post(
            "https://api.tavily.com/search",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "query": query,
                "include_answer": True,
                "include_raw_content": True,
                "max_results": max_results,
                "search_depth": "basic"
            },
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        # Process results
        if not data.get("results"):
            return "No search results found"

        # Combine the most relevant information
        if data.get("answer"):
            return data["answer"]

        contents = [result["content"] for result in data["results"][:max_results] if result.get("content")]
        return "\n\n".join(contents) if contents else "No content available in results"

    except requests.exceptions.RequestException as e:
        return f"Search failed: {str(e)}"
    except json.JSONDecodeError:
        return "Invalid response from search API"
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Create the LangChain Tool
WebSearchTool = Tool.from_function(
    func=web_search,
    name="WebSearchTool",
    description="Searches the web to retrieve missing context. Use when you need current information or when existing context is insufficient."
)
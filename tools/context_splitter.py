from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
import json

def build_context_splitter_tool(llm):
    prompt = PromptTemplate.from_file("prompts/context_splitter_prompt.txt")
    chain = prompt | llm

    def _safe_run(input: str) -> str:
        try:
            result = chain.invoke({"input": input})
            # Ensure the output is valid JSON
            json.loads(result)  # Validate it's proper JSON
            return result
        except json.JSONDecodeError:
            # Fallback if the LLM doesn't return proper JSON
            return json.dumps({"context": "", "question": input})
        except Exception as e:
            return json.dumps({"context": "", "question": input})

    return Tool.from_function(
        func=_safe_run,
        name="ContextSplitter",
        description="Splits user input into 'context' and 'question' fields"
    )
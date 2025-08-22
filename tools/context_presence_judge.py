from langchain.tools import Tool
from langchain.prompts import PromptTemplate

def build_context_presence_tool(llm):
    prompt = PromptTemplate.from_file("prompts/context_judge_prompt.txt")
    chain = prompt | llm  # Modern runnable syntax

    def _safe_run(input: str) -> str:
        return chain.invoke({"input": input})

    return Tool.from_function(
        func=_safe_run,
        name="ContextPresenceJudge",
        description="Checks if context is present in user input"
    )
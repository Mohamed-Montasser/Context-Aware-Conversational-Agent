from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

def build_context_relevance_tool(llm):
    prompt = PromptTemplate.from_file("prompts/context_relevance_prompt.txt")
    chain = prompt | llm  # modern runnable

    def _safe_run(context_plus_question: str) -> str:
        """
        context_plus_question is expected to be:
        <context>\n<question>
        """
        try:
            context, question = context_plus_question.split("\n", 1)
        except ValueError:
            context, question = context_plus_question, ""
        return chain.invoke({"context": context, "question": question})

    return Tool.from_function(
        func=_safe_run,
        name="ContextRelevanceChecker",
        description="Decides if the provided context is relevant to the question"
    )
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from app.services.query_schema import PropertyQuery
from app.services.gemini_llm import get_gemini_llm

def extract_filters(user_message: str) -> PropertyQuery:
    parser = PydanticOutputParser(pydantic_object=PropertyQuery)

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a real estate assistant. "
         "Extract structured property search filters from the user message. "
         "If a field is not mentioned, return null."),
        ("human",
         "{query}\n\n{format_instructions}")
    ])

    llm = get_gemini_llm()

    chain = prompt | llm | parser

    return chain.invoke({
        "query": user_message,
        "format_instructions": parser.get_format_instructions()
    })

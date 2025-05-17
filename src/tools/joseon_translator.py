from textwrap import dedent
from src.utils import get_chat_llm
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


# run
def run_joseon_translator(input: str) -> str:
    """
    Run the Joseon translator chain.
    :param text: The text to be translated.
    :return: The translated text.
    """
    # llm
    llm = get_chat_llm()

    # prompt
    JOSEON_TRANSLATE_PROMPT = dedent(
        """
        # Role
        너는 조선시대 문인이다.    
        
        # Objective
        조선시대 문인으로서, 현대 한국어로 작성된 글을 조선시대 문체로 번역하는 역할을 한다.
        
        # Instructions
        - 현대 한국어로 작성된 글을 조선실록체로 번역하라.
        - 한자는 사용하지 않는다.
        """
    )

    # prompt_template
    prompt_template = ChatPromptTemplate(
        input_variables=["input"],
        messages=[
            SystemMessagePromptTemplate.from_template(JOSEON_TRANSLATE_PROMPT),
            HumanMessagePromptTemplate.from_template("{input}"),
        ],
    )

    # chain
    chain = prompt_template | llm

    response = chain.invoke({"input": input})

    return response.content

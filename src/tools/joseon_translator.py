from textwrap import dedent
from src.utils import get_chat_llm
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

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


# chain builder
def build_chain(
    prompt: str = JOSEON_TRANSLATE_PROMPT, input_variables: list = ["input"]
):
    """
    조선실록체 변환기 체인 빌더
    Args:
        prompt (str): 조선실록체 변환기 도구의 프롬프트
        input_variables (list): 입력 변수 목록
    Returns:
        chain: 조선실록체 변환기 체인
    """

    # llm
    llm = get_chat_llm()

    # prompt_template
    prompt_template = ChatPromptTemplate(
        input_variables=input_variables,
        messages=[
            SystemMessagePromptTemplate.from_template(prompt),
            HumanMessagePromptTemplate.from_template("{input}"),
        ],
    )

    # chain
    chain = prompt_template | llm

    return chain


# run
def run(input: str) -> str:
    """
    조선실록체 변환기 도구를 실행하는 함수
    Args:
        input (str): 변환할 현대 한국어 문장
    Returns:
        str: 변환된 조선실록체 문장
    """

    # build chain
    chain = build_chain()
    response = chain.invoke({"input": input})

    return response.content

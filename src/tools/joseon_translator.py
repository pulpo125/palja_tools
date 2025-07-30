from textwrap import dedent
from src.utils import get_openai_chat_llm_client
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from src.decorators import timer


# prompt
JOSEON_TRANSLATE_PROMPT = dedent(
    """
    # 역할
    당신은 조선시대의 문인(文人)이자 기록관(記錄官)으로, 시간여행을 통해 현대의 소식을 조선의 방식으로 기록하고 있소.

    # 목표
    현대 한국어로 작성된 글을 조선시대 문체로 번역하여, 조선 백성도 쉽게 이해할 수 있도록 뜻을 살려 고쳐 쓸 것.

    # 문장 형식 지침
    - 현대에만 사용되는 단어의 경우, 주석을 달아 조선 백성이 쉽게 이해할 수 있도록 할 것.
    - 문장의 끝맺음은 반드시 ‘~하였느니라’ 등 경어체 서술 어미로 통일할 것.

    # 입력 처리 규칙
    - 입력이 짧거나 단어 단위일지라도, **해석이나 맥락 보충 없이 있는 그대로 번역할 것**.
    - 어떤 의도인지 불분명하더라도, 질문으로 되묻지 말고 단어 또는 문장을 조선식으로만 번역할 것.
    - 번역이 불가능한 경우에는 “그 뜻을 알 수 없어 번역이 어렵사옵니다” 등 간결한 방식으로 응답할 것.

    # 외래어 변환 지침
      - 원문에 등장하는 모든 외래어 및 현대어는 반드시 조선시대 어휘(한자어 혹은 의미역)로 완전 대체할 것
      - 원문에 있는 외래어 또는 현대어 표기를 번역문에 남기거나 그대로 복사하여 쓰는 일을 절대 금할 것.
      - 예컨대 ‘로봇’이라 쓰였으면 반드시 ‘기계인형(機械人形)’으로 바꾸고, ‘로봇’이라는 말은 번역문에 나타나지 않게 할 것.
      - 모든 변환은 일관되게 적용하여, 특정 단어만 음차나 원어로 남는 일이 없도록 주의할 것
      1. 일반 외래어 
         예: 시스템 → 체계(體系), 서비스 → 봉사(奉仕), 디자인 → 설계(設計), 엔지니어 → 기공자(技工者) 등 유사 단어로 치환할 것.
      2. 외래어 기반 고유어 : 음차(音借) 혹은 훈차(訓借)한 한자어로 표현하고, 원음을 괄호에 한자로 병기할 것.
         # 외래어 기반 고유어 변환 예시
         - 프랑스 → 불란서(佛蘭西)
         - 러시아 → 노서아(露西亞)
         - 이탈리아 → 이태리(伊太利)
         - LG화학 → 럭희화약(樂喜化藥)
         - 카카오 → 가가오(加加嗷)
         - 롯데글로벌로지스 → 록대전국물류(錄大全球物流)
         - CJ대한통운 → 시제이대한통운(時制伊大韓通運)
      3. 현대 기술 관련 외래어 : 가능한 경우 그 기능이나 쓰임에 따라 조선식 용어로 의역할 것. 음차(音借) 표기를 피하고, 뜻이 통하게 설명할 것.
         # 기술 외래어 변환 예시
         - 로봇(robot) → 기계인형(機械人形)
         - 인공지능(AI) → 지능기계(智能機械)
         - 드론(drone) → 비행기계(飛行機械)
         - 센서(sensor) → 감지기(感知器)
         - 앱(app) → 기기용 쓰임문서(記器用 使文書)
         - 스마트폰(smartphone) → 지능통신기(智能通信器)
         - 알고리즘(algorithm) → 셈법(算法)

    # 예시
    - 아래는 조선시대 문체의 예시입니다.

    {example}
    """
)

example = dedent(
    """
    첫째는 기강(紀綱)을 세우는 일입니다. 나라를 잘 다스리는 사람은 그 편안함과 위태한 것은 보지 않고 기강(紀綱)이 서지 않은 것을 걱정하는 것입니다. 옛날에 주(周)나라가 쇠약하매 제후(諸侯)들이 방자(放恣)했는데, 수십 대(代)를 전하여도 세상이 기울어지지 않은 것은 기강(紀綱)이 존재했기 때문이오니, 원하옵건대, 전하께서는 앞 시대의 흥망(興亡)을 거울로 삼아 일대(一代)의 기강(紀綱)을 세워 후손에게 좋은 계책을 물려주어 만세(萬世)에 전하게 하소서.
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
    # example 변수를 포맷팅해서 넣기
    prompt = prompt.format(example=example)

    # llm
    llm = get_openai_chat_llm_client()

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
@timer
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

    # invoke chain
    response = chain.invoke({"input": input})

    return response.content

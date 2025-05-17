from langchain_openai import ChatOpenAI

from src.config import cfg


def get_openai_chat_llm():
    llm = ChatOpenAI(
        model=cfg.openai.llm_model,
        max_tokens=cfg.openai.llm_max_tokens,
        api_key=cfg.openai.api_key,
        temperature=0,
    )
    return llm

from langchain_openai import ChatOpenAI

from src.config import cfg


# =========================================================
# Clients
# =========================================================
class ClientManager:
    """
    A singleton class to manage llm clients.
    'instance' 속성이 없으면 새 인스턴스를 생성, 있으면 동일한 인스턴스를 반환
    """

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ClientManager, cls).__new__(cls)
        return cls.instance


client_manager = ClientManager()


def get_openai_chat_llm_client():
    key = "ChatOpenAI"
    if not hasattr(client_manager, key):
        chat_llm = ChatOpenAI(
            model=cfg.openai.llm_model,
            max_tokens=cfg.openai.llm_max_tokens,
            api_key=cfg.openai.api_key,
            temperature=0,
        )
        setattr(client_manager, key, chat_llm)  # 생성한 인스턴스를 속성으로 저장
    return getattr(client_manager, key)

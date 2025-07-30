import logging
import json
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


# ==================================================
# Logger
# ==================================================


logger = logging.getLogger()

logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def disable_logger():
    logger.setLevel(logging.WARNING)


def slog(
    msg: str,
    style: str = "BLUE",
    log: str = "info",
    dump: bool = True,
    notify_slack: bool = False,
) -> str:
    """Stylish log message.

    Args:
        msg (str): The message to log.
        color (str): The color of the message. Defaults to "BLUE".
        log (str): The log level. Defaults to "info".
        dump (bool): The dump flag. Defaults to True.

    Returns:
        str: The stylish message.
    """
    styles = {
        "ENDC": "\033[0m",
        "OKBLUE": "\033[94m",
        "OKCYAN": "\033[96m",
        "OKGREEN": "\033[92m",
        "BOLD": "\033[1m",
        "UNDERLINE": "\033[4m",
        "BLUE": "\033[34m",
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "ORANGE": "\033[33m",
        "PURPLE": "\033[35m",
        "CYAN": "\033[36m",
        "LIGHTGRAY": "\033[37m",
        "DARKGRAY": "\033[90m",
        "LIGHTRED": "\033[91m",
        "YELLOW": "\033[93m",
        "PINK": "\033[95m",
        "DARKORANGE": "\033[38;5;214m",
        "GRAPEFRUIT": "\033[38;5;208m",
    }
    try:
        if dump:
            msg = pretty_dict(msg)
            msg = msg.strip('"')  # remove redundant quotes
    except:
        pass

    if style:
        stylish_msg = f"{styles[style]}{msg}{styles['ENDC']}"
    else:
        stylish_msg = msg

    if log == "info":
        logger.info(stylish_msg)
    elif log == "warning":
        if notify_slack:
            logger.warning(stylish_msg)
        else:
            logger.warning(stylish_msg)
    elif log == "error":
        if notify_slack:
            logger.error(stylish_msg)
        else:
            logger.error(stylish_msg)
    elif log == "critical":
        logger.critical(stylish_msg)
    else:
        print(stylish_msg)

    return stylish_msg


def log_info(msg: str, dump: bool = True) -> None:
    """Stylish info log.

    Args:
        msg (str): The message to log.
        dump (bool): The dump flag. Defaults to True.
    """
    slog(msg, style="GREEN", dump=dump)


def log_warning(msg: str, dump: bool = False, prefix: bool = True) -> str:
    """Stylish warning log.

    Args:
        msg (str): The message to log.
        dump (bool): The dump flag.
        prefix (bool): The prefix flag.
        notify_slack (bool): The notify slack flag.
    """
    if prefix:
        msg = f"[WARNING] {msg}"
    return slog(msg, style="GRAPEFRUIT", log="warning", dump=dump)


def log_error(msg: str, dump: bool = False) -> None:
    """Stylish error log.

    Args:
        msg (str): The message to log.
        dump (bool): The dump flag. Defaults to False.
        notify_slack (bool): The notify slack flag. Defaults to False.
    """
    slog(msg, style="GRAPEFRUIT", log="error", dump=dump)


# ==================================================
# General Utilities
# ==================================================


def pretty_dict(s: str) -> str:
    """Pretty print dictionary.

    Args:
        s (str): The dictionary to pretty print.

    Returns:
        str: The pretty printed dictionary.
    """
    return json.dumps(s, indent=2, ensure_ascii=False)

import json
from dataclasses import asdict

import requests
from requests.exceptions import ReadTimeout

from item_parser.config import RESULT_PATH
from item_parser.dataclasses import ItemData


def get_json_response(url: str, timeout: int | float = 5) -> dict:
    """Делает запрос на ссылку url с таймаутом timeout"""
    try:
        response = requests.get(url=url, timeout=timeout)
    except ReadTimeout as err:
        raise ReadTimeout(f"Истекло время ожидания ответа. url={url}") from err
    response.raise_for_status()
    if response.headers["content-type"] != "application/json":
        raise ValueError(
            "Ожидается что заголовок 'Content-Type' "
            f"будет 'application/json'. url={url}"
        )
    return response.json()


def write_items_json(items: dict[str, ItemData]) -> None:
    """Записывает данные предметов в json"""
    with open(RESULT_PATH, "w", encoding="UTF-8") as file:
        json.dump(
            [asdict(v) for _, v in items.items()], file, indent=2, ensure_ascii=False
        )

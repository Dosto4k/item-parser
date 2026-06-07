#!/usr/bin/env -S uv run --script

from item_parser.common import write_items_json
from item_parser.parsers import QuestParser, QuestSourcesParser


def main() -> None:
    quests_links = QuestSourcesParser().get_result()
    items = QuestParser(quests_links).get_result()
    write_items_json(items=items)


if __name__ == "__main__":
    main()

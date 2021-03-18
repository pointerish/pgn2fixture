import re
from typing import Dict, List


def clean(raw_pgn: str) -> List:
    str_tags = re.split(r'\]', raw_pgn, re.DOTALL)
    def cleaner(x): return x.replace('\n', '').replace('[', '')
    return list(map(cleaner, str_tags))


def extract_tag_roster(game: List) -> Dict:
    tags = {}
    for item in game[:-1]:
        key = item.split('"')[0].lower().strip()
        value = item.split('"')[1]
        tags.update({key: value})
    tags.update({'moves': game[-1]})
    return tags

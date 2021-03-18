import re
from typing import Dict, List


def clean(raw_pgn: str) -> List:
    """
    The clean method cleans the raw PGN data
    and returns each tag as an element in a list
    """
    str_tags = re.split(r'\]', raw_pgn, re.DOTALL)
    def cleaner(x): return x.replace('\n', '').replace('[', '')
    return list(map(cleaner, str_tags))


def extract_tag_roster(game: List) -> Dict:
    """
    The extract_tag_roster transforms the tags list into a 
    dictionary with the tag name as keys and the tag values as values
    """
    tags = {}
    for item in game[:-1]:
        key = item.split('"')[0].lower().strip()
        value = item.split('"')[1]
        tags.update({key: value})
    tags.update({'moves': game[-1]})
    return tags

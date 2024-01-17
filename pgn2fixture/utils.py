import re
from typing import Dict, List


def clean(raw_pgn: str) -> List:
    """
    The clean method cleans the raw PGN data
    and returns each tag as an element in a list
    """
    split_game = raw_pgn.split(' 1. ')
    moves = split_game[1]
    str_tags = re.split(r'\]', split_game[0], re.DOTALL)
    def cleaner(x): return x.replace('\n', '').replace('[', '')
    response = list(map(cleaner, str_tags))
    return response.append(f'1. {moves}')


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

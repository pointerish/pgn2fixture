from utils import clean
from utils import extract_tag_roster


class Game:

    def __init__(self, raw_game_data) -> None:
        self.tags = extract_tag_roster(clean(raw_game_data))

    def __str__(self):
        return f'{self.white} - {self.black} | {self.event}'

    @property
    def event(self):
        return self.tags['event']

    @property
    def site(self):
        return self.tags['site']

    @property
    def date(self):
        return self.tags['date']

    @property
    def round(self):
        return int(self.tags['round'])

    @property
    def result(self):
        return self.tags['result']

    @property
    def white(self):
        return self.tags['white']

    @property
    def black(self):
        return self.tags['black']

    @property
    def moves(self):
        return self.tags['moves']

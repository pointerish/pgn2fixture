from . import utils
from typing import Dict, List


class Game:
    """ 
    This is a class for PGN tag extraction and handling. 
      
    Attributes: 
        raw_game_data (str): The PGN game string.
    """

    def __init__(self, raw_game_data) -> None:
        """
        The init method creates the instance variable tags.
        The variable tags is a dictionary containing all PGN tags/data.
        """
        self.tags = utils.extract_tag_roster(utils.clean(raw_game_data))

    def __str__(self) -> str:
        return f'{self.white} - {self.black} | {self.event}'

    def __repr__(self) -> str:
        return f'{self.white} - {self.black} | {self.event}'

    @property
    def event(self) -> str:
        """
        The event property returns the event PGN tag
        """
        return self.tags['event']

    @property
    def site(self) -> str:
        """
        The site property returns the site PGN tag
        """
        return self.tags['site']

    @property
    def date(self) -> str:
        """
        The date property returns the date PGN tag
        """
        return self.tags['date']

    @property
    def round(self) -> int:
        """
        The round property returns the round PGN tag
        """
        return int(self.tags['round'])

    @property
    def result(self) -> str:
        """
        The result property returns the result PGN tag
        """
        return self.tags['result']

    @property
    def white(self) -> str:
        """
        The white property returns the white PGN tag
        """
        return self.tags['white']

    @property
    def black(self) -> str:
        """
        The black property returns the black PGN tag
        """
        return self.tags['black']

    @property
    def moves(self) -> str:
        """
        The moves property returns the game moves including the result
        """
        return self.tags['moves']

    def to_fixture(self, model, pk) -> Dict:
        """
        The to_fixture method returns the entire PGN
        data as a dictionary ready to dump into a JSON file
        to create Django fixtures
        """
        fixture = {
            "model": model,
            "pk": pk,
            "fields": self.tags
        }
        return fixture
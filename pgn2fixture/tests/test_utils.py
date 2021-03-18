import unittest
from .. import utils


class TestUtils(unittest.TestCase):

    def setUp(self) -> None:
        self.pgn_string = '''[Event "US Championship 1963/64"][Site "New York, NY USA"][Date "1964.01.01"][EventDate "1963.??.??"][Round "11"][Result "0-1"][White "Anthony Saidy"][Black "Robert James Fischer"][ECO "A33"][WhiteElo "?"][BlackElo "?"][PlyCount "112"]1. c4 0-1'''

    def test_clean(self):
        result = ['Event "US Championship 1963/64"', 'Site "New York, NY USA"', 'Date "1964.01.01"', 'EventDate "1963.??.??"', 'Round "11"', 'Result "0-1"',
                  'White "Anthony Saidy"', 'Black "Robert James Fischer"', 'ECO "A33"', 'WhiteElo "?"', 'BlackElo "?"', 'PlyCount "112"', '1. c4 0-1']
        self.assertEqual(utils.clean(self.pgn_string), result)

    def test_extract_tag_roster(self):
        result = {'event': 'US Championship 1963/64', 'site': 'New York, NY USA', 'date': '1964.01.01', 'eventdate': '1963.??.??', 'round': '11', 'result': '0-1',
                  'white': 'Anthony Saidy', 'black': 'Robert James Fischer', 'eco': 'A33', 'whiteelo': '?', 'blackelo': '?', 'plycount': '112', 'moves': '1. c4 0-1'}
        self.assertEqual(utils.extract_tag_roster(self.pgn_string), result)

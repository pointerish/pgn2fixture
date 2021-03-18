import unittest
from .. import Game


class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        with open('../pgn_samples/saidy-fischer.pgn', 'r') as pgn:
            pgn_string = pgn.read().replace("\n", " ")

        self.game = Game(pgn_string)

    
    def test_event(self):
        self.assertEqual(self.game.event, 'US Championship 1963/64')
    
    def test_site(self):
        self.assertEqual(self.game.site, 'New York, NY USA')

    def test_date(self):
        self.assertEqual(self.game.date, '1964.01.01')

    def test_round(self):
        self.assertEqual(self.game.round, 11)

    def test_result(self):
        self.assertEqual(self.game.result, '0-1')

    def test_white(self):
        self.assertEqual(self.game.white, 'Anthony Saidy')

    def test_black(self):
        self.assertEqual(self.game.black, 'Robert James Fischer')

    def test_tags(self):
        self
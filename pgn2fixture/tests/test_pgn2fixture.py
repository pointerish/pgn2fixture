import unittest
from .. import pgn2fixture


class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        pgn_string = '''
        [Event "US Championship 1963/64"]
        [Site "New York, NY USA"]
        [Date "1964.01.01"]
        [EventDate "1963.??.??"]
        [Round "11"]
        [Result "0-1"]
        [White "Anthony Saidy"]
        [Black "Robert James Fischer"]
        [ECO "A33"]
        [WhiteElo "?"]
        [BlackElo "?"]
        [PlyCount "112"]


        1. c4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Ndb5 Bb4 7. a3 Bxc3+ 8. Nxc3 d5 9. e3 O-O 10. cxd5 exd5 11. Be2 Bf5 12. Nb5 Qb6 13. O-O a6 14. Nd4 Nxd4 15. Qxd4 Qxd4 16. exd4 Rac8 17. Bd1 Bc2 18. Be3 Bxd1 19. Rfxd1 Rc2 20. Rd2 Rfc8 21. Rxc2 Rxc2 22. Rc1 Rxc1+ 23. Bxc1 Nd7 24. Kf1 Nf8 25. Ke2 Ne6 26. Kd3 h5 27. Be3 Kh7 28. f3 Kg6 29. a4 Kf5 30. Ke2 g5 31. Kf2 Nd8 32. Bd2 Kg6 33. Ke3 Ne6 34. Kd3 Kf5 35. Be3 f6 36. Ke2 Kg6 37. Kd3 f5 38. Ke2 f4 39. Bf2 Ng7 40. h3 Nf5 41. Kd3 g4 42. hxg4 hxg4 43. fxg4 Nh6 44. Be1 Nxg4 45. Bd2 Kf5 46. Be1 Nf6 47. Bh4 Ne4 48. Be1 Kg4 49. Ke2 Ng3+ 50. Kd3 Nf5 51. Bf2 Nh4 52. a5 Nxg2 53. Kc3 Kf3 54. Bg1 Ke2 55. Bh2 f3 56. Bg3 Ne3 0-1
        '''
        self.game = pgn2fixture.Game(pgn_string)

    
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

if __name__ == '__main__':
    unittest.main()
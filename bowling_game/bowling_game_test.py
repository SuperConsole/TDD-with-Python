import unittest
import bowling_game

class BowlingGameTest(unittest.TestCase):
    game    = None

    def setUp(self):
        self.game = bowling_game.BowlingGame()

    def test_all_gutter_game(self):
        #ALL GUTTER
        #score: 0
        self.record_n_shot(0, 20)
        self.assertEqual(0, self.game.get_total_score())

    def test_all_one_point_game(self):
        #ALL ONE PIN
        #score:20
        self.record_n_shot(1, 20)
        self.assertEqual(20, self.game.get_total_score())

    def test_has_one_spare_game(self):
        #ONE SPARE
        #score: 18
        self.game.record_shot(3)
        self.game.record_shot(7)
        self.game.record_shot(4)
        self.record_n_shot(0, 17)
        self.assertEqual(18, self.game.get_total_score())

    def test_has_no_spare_game_2(self):
        #NO SPARE
        #score: 13
        self.game.record_shot(2)
        self.game.record_shot(5)
        self.game.record_shot(5)
        self.game.record_shot(1)
        self.record_n_shot(0, 16)
        self.assertEqual(13, self.game.get_total_score())

    def record_n_shot(self, point, n):
        for i in range(1,n+1):
            self.game.record_shot(point)

if __name__ ==  "__main__":
    unittest.main()
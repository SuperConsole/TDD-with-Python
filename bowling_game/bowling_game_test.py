import unittest
import bowling_game

class BowlingGameTest(unittest.TestCase):
    game=None

    def setUp(self):
        self.game = bowling_game.BowlingGame()

    def test_all_gutter_game(self):
        self.record_n_shot(0, 20)
        
        self.assertEqual(0, self.game.get_total_score())

    def test_all_one_point_game(self):
        self.record_n_shot(1, 20)
        
        self.assertEqual(20, self.game.get_total_score())

    def record_n_shot(self, point, n):
        for i in range(1,n+1):
            self.game.record_shot(point)

if __name__ == "__main__":
    unittest.main()
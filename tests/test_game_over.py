import unittest
import numpy as np
import src.gameplay as gp


class TestGameOver(unittest.TestCase):

    def setUp(self):
        self.n_rows = 6
        self.n_cols = 7
        self.plr = 1
        self.board_1s = np.ones((self.n_rows, self.n_cols), dtype=np.int8)
        self.board_0s = np.zeros((self.n_rows, self.n_cols), dtype=np.int8)

    def test_no_more_space(self):
        res = gp.game_over(self.board_1s, self.n_cols, self.plr)
        self.assertTrue(res)

    def test_four_found(self):
        self.board_0s[0][:4] = [1, 1, 1, 1]
        self.plr = gp.switch_player(self.plr)
        res = gp.game_over(self.board_0s, self.n_cols, self.plr)
        self.assertTrue(res)

    def test_four_not_found(self):
        self.board_0s[0][:3] = [1, 1, 1]
        res = gp.game_over(self.board_0s, self.n_cols, self.plr)
        self.assertFalse(res)

    def test_empty_board(self):
        res = gp.game_over(self.board_0s, self.n_cols, self.plr)
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()

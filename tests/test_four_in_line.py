import unittest
import numpy as np
import numpy.testing as nptest
import src.gameplay as gp


class TestFourInLine(unittest.TestCase):
    n_rows = None
    n_cols = None
    board_with_four = None
    board_with_four_in_1st_col = None
    empty_board = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.n_rows = 6
        cls.n_cols = 7
        cls.board_with_four = np.zeros((cls.n_rows, cls.n_cols), dtype=np.int8)
        cls.empty_board = cls.board_with_four.copy()
        cls.board_with_four[0][:4] = [1, 1, 1, 1]

    def test_four_1s_in_row(self):
        res = gp.four_in_any_row(self.board_with_four)
        self.assertTrue(res)

    def test_four_2s_in_row(self):
        self.board_with_four[0][:4] = [2, 2, 2, 2]
        res = gp.four_in_any_row(self.board_with_four)
        self.assertTrue(res)

    def test_no_fours(self):
        res = gp.four_in_any_row(self.empty_board)
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()

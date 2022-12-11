import unittest
import numpy as np
import numpy.testing as nptest
import src.gameplay as gp


class TestPiecePlacement(unittest.TestCase):

    def setUp(self):
        self.n_rows = 6
        self.n_cols = 7
        self.board = np.zeros((self.n_rows, self.n_cols))
        self.test_board = self.board.copy()

    def test_new_place(self):
        """
        Check if placing a piece in an empty spot on board
        changes the board layout properly.
        :return:
        """
        row, col, plr = 2, 2, 1
        res = gp.place_piece(self.board, row, col, plr, self.n_rows, self.n_cols)
        self.test_board[row, col] = 1
        self.assertIsNone(nptest.assert_array_equal(self.board, self.test_board))
        self.assertTrue(res)

    def test_piece_on_taken_place(self):
        """
        Check if board remains unchanged after trying to
        place a piece in an already taken place.
        :return:
        """
        row, col, plr = 2, 2, 1
        gp.place_piece(self.board, row, col, plr, self.n_rows, self.n_cols)
        board_after_1st_piece_placed = self.board.copy()
        with self.assertRaises(IndexError):
            res = gp.place_piece(self.board, row, col, plr, self.n_rows, self.n_cols)
        self.assertIsNone(nptest.assert_array_equal(self.board, board_after_1st_piece_placed))
        self.assertFalse(res)

    def test_outside_board(self):
        """
        Check if board remains unchanged after trying to
        place a piece outside of board dimensions.
        :return:
        """
        row, col, plr = self.n_rows, 2, 1
        with self.assertRaises(IndexError):
            res = gp.place_piece(self.board, row, col, plr, self.n_rows, self.n_cols)
        self.assertIsNone(nptest.assert_array_equal(self.board, self.test_board))
        self.assertFalse(res)

    def test_negative_indices(self):
        """
        Check if board remains unchanged after trying to
        place a piece in negative indices.
        :return:
        """
        row, col, plr = -1, -3, 1
        with self.assertRaises(IndexError):
            res = gp.place_piece(self.board, row, col, plr, self.n_rows, self.n_cols)
        self.assertIsNone(nptest.assert_array_equal(self.board, self.test_board))
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()

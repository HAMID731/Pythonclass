from unittest import TestCase

import Board

class TestBoard(TestCase):
    def setUp(self):
        self.board = Board.Board()

    def test_make_move_valid(self):
        self.assertTrue(self.board.make_move(0, 0, "X"))
        self.assertEqual(self.board.board[0][0], "X")

    def test_make_move_invalid(self):
        self.board.make_move(0, 0, "X")
        self.assertFalse(self.board.make_move(0, 0, "O"))

    def test_check_win_row(self):
        self.board.board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(self.board.check_win(), "X")

    def test_check_win_column(self):
        self.board.board = [["O", " ", " "], ["O", " ", " "], ["O", " ", " "]]
        self.assertEqual(self.board.check_win(), "O")

    def test_check_win_diagonal(self):
        self.board.board = [["@", " ", " "], [" ", "@", " "], [" ", " ", "@"]]
        self.assertEqual(self.board.check_win(), "@")

    def test_check_win_no_win(self):
        self.assertIsNone(self.board.check_win())

    def test_is_board_full_true(self):
        self.board.board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.assertTrue(self.board.is_board_full())

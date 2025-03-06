import unittest
from Board import Board


class TestTicTacToe(unittest.TestCase):

    def test_make_move_valid(self):
        board = Board()
        self.assertTrue(board.make_move(0, 0, 'X'))
        self.assertEqual(board.board[0][0], 'X')

    def test_make_move_invalid(self):
        board = Board()
        board.make_move(0, 0, 'X')
        self.assertFalse(board.make_move(0, 0, 'O'))

    def test_is_full_false(self):
        board = Board()
        self.assertFalse(board.is_full())


    def test_check_winner_row(self):
        board = Board()
        board.make_move(0, 0, 'X')
        board.make_move(0, 1, 'X')
        board.make_move(0, 2, 'X')
        self.assertTrue(board.check_winner('X'))

    def test_check_winner_column(self):
        board = Board()
        board.make_move(0, 0, 'O')
        board.make_move(1, 0, 'O')
        board.make_move(2, 0, 'O')
        self.assertTrue(board.check_winner('O'))

    def test_check_winner_diagonal(self):
        board = Board()
        board.make_move(0, 0, 'X')
        board.make_move(1, 1, 'X')
        board.make_move(2, 2, 'X')
        self.assertTrue(board.check_winner('X'))

    def test_check_winner_other_diagonal(self):
        board = Board()
        board.make_move(0, 2, 'O')
        board.make_move(1, 1, 'O')
        board.make_move(2, 0, 'O')
        self.assertTrue(board.check_winner('O'))


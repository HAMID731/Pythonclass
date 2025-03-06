import unittest
from src import swap

class TestSwapFirstLetters(unittest.TestCase):

  def test_basic_swap(self):
    self.assertEqual(swap.swap_first_letters("abc", "xyz"), ("xyc", "abz"))

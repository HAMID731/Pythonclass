import unittest
from src import character_frequency

class TestCountLetters(unittest.TestCase):

    def test_basic_string(self):
        self.assertEqual(character_frequency.count_letters("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_mixed_case(self):
        self.assertEqual(character_frequency.count_letters("Hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_with_numbers_and_symbols(self):
        self.assertEqual(character_frequency.count_letters("hello123world!"), {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})

    def test_empty_string(self):
        self.assertEqual(character_frequency.count_letters(""), {})

    def test_string_with_spaces(self):
      self.assertEqual(character_frequency.count_letters("hello world"),{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})

    def test_string_with_repeating_letters(self):
      self.assertEqual(character_frequency.count_letters("aaaaabbbbcccdd"),{'a': 5, 'b': 4, 'c': 3, 'd': 2})


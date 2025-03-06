from unittest import TestCase

from src import find_count

class TestFindCount(TestCase):
    def test_find_count(self):
        self.assertEqual(find_count.find_count("semicolon", "o"), 2)

    def test_find_count_no_letter(self):
        self.assertEqual(find_count.find_count("apple", "z"), 0)

    def test_find_count_multiple_letters(self):
        self.assertEqual(find_count.find_count("banana", "a"), 3)

    def test_find_count_empty_string(self):
        self.assertEqual(find_count.find_count("", "a"), 0)

    def test_find_count_uppercase(self):
        self.assertEqual(find_count.find_count("Banana", "B"), 1)
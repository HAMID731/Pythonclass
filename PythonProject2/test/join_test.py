import unittest
from src import join

class TestJoinClean(unittest.TestCase):
    def test_join_clean_basic(self):
        my_parts = ["Hel", "lo!", "Wor", "ld?", "123"]
        expected_output = "HelloWorld"
        self.assertEqual(join.join_clean(my_parts), expected_output)

    def test_join_clean_empty_parts(self):
        my_parts = []
        expected_output = ""
        self.assertEqual(join.join_clean(my_parts), expected_output)

    def test_join_clean_only_non_alpha(self):
        my_parts = ["123", "!@#", "$%^"]
        expected_output = ""
        self.assertEqual(join.join_clean(my_parts), expected_output)

    def test_join_clean_some_empty_strings(self):
        my_parts = ["Hello", "", "World", "!!!"]
        expected_output = "HelloWorld"
        self.assertEqual(join.join_clean(my_parts), expected_output)

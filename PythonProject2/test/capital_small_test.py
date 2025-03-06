from unittest import TestCase

from src import capital_small

class TestCapitalAndSmall(TestCase):

    def test_capital_and_small(self):
        self.assertEqual(capital_small.separate_letters("SemiCOlOn"),"SCOOemiln")

    def test_only_capital(self):
        self.assertEqual(capital_small.separate_letters("SEMICOLON"),"SEMICOLON")

    def test_take_only_capital(self):
        self.assertEqual(capital_small.separate_letters("semicolon"),"semicolon")

    def test_does_not_take_numbers(self):
        self.assertEqual(capital_small.separate_letters("semIcOLon123"),"IOLsemcon")
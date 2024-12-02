from unittest import TestCase
import semicolon_store  

class TestSemicolonStore(TestCase):
	def test_that_calculate_totals_function_exists(self):
		semicolon_store.calculate_totals(["Milk"], [50.0], [2])

	def test_that_calculate_totals_returns_correct_values(self):
		actual = semicolon_store.calculate_totals(["Milk", "Bread"], [50.0, 30.0], [2, 3])
		expected = 183.825
		self.assertAlmostEqual(actual, expected, places=2)

		actual = semicolon_store.calculate_totals(["Eggs"], [40.0], [4])
		expected = 154.8
		self.assertAlmostEqual(actual, expected, places=2)

	def test_that_calculate_totals_does_not_accept_strings(self):
		self.assertRaises(TypeError, semicolon_store.calculate_totals, ["Milk"], ["fifty"], [2])
		self.assertRaises(TypeError, semicolon_store.calculate_totals, ["Milk"], [50.0], ["two"])

	def test_that_ask_for_payment_function_exists(self):
		semicolon_store.ask_for_payment(200)

	

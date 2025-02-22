from unittest import TestCase
import divide_or_square
import future_investment

class TestDivideOrSquare(TestCase):
	def test_that_is_divisible_function_exists(self):
		divide_or_square.get_remainder(3)

	def test_that_divisible_function_returns_correct_value(self):
		actual = divide_or_square.get_remainder(45)
		expected = 6.71
		self.assertEqual(actual, expected)
		actual = divide_or_square.get_remainder(55)
		expected = 7.42
		self.assertEqual(actual, expected)
	
	def test_that_you_can_enter_a_float_value(self):
		actual = divide_or_square.get_remainder(32.5)
		expected = 2.5
		self.assertEqual(actual, expected)
		
	
	def test_that_it_does_not_accept_string_values(self):
		self.assertRaises(TypeError, divide_or_square.get_remainder, "hamid")

	def test_that_it_does_not_allow_zero_value(self):
		self.assertRaises(ZeroDivisionError, divide_or_square.get_remainder, 0)

	def test_that_it_allows_negative_number(self):
		self.assertRaises(ValueError, divide_or_square.get_remainder, -5)

	def test_that_it_disallow_number_greater_than_one_thousand(self):
		self.assertRaises(ValueError, divide_or_square.get_remainder, 1001)









	def test_that_is_investent_function_exists(self):
		future_investment.get_investment(2,3,4)

	def test_that_investment_function_returns_correct_value(self):
		actual = future_investment.get_investment(2000,100,4)
		expected = 200000002000
		self.assertEqual(actual, expected)
		actual = future_investment.get_investment(1000,50,5)
		expected = 312500001000
		self.assertEqual(actual, expected)

	def test_that_you_can_enter_a_float_value(self):
		actual = future_investment.get_investment(320.45,20,2)
		expected = 128320
		self.assertEqual(actual, expected)



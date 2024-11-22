from unittest import TestCase
import divide_or_square

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





from unittest import TestCase
import number

class TestNumber(TestCase):
	def test_multiplication(self):
		number.get_multiplication(2,3)
		
	def test_that_number_function_returns_correct_value(self):
		actual = number.get_multiplication(6,2)
		expected = 12
		self.assertEqual(actual, expected)
		actual = number.get_multiplication(9,5)
		expected = 45
		self.assertEqual(actual, expected)

	def test_that_number_accepts_zero_value(self):
		actual = number.get_multiplication(2,0)
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_number_accepts_negative_value(self):
		actual = number.get_multiplication(-2,5)
		expected = -10
		self.assertEqual(actual, expected)
		actual = number.get_multiplication(-2,-5)
		expected = 10
		self.assertEqual(actual, expected)
		actual = number.get_multiplication(2,-5)        
		expected = -10
		self.assertEqual(actual, expected)
	
		
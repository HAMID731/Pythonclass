from unittest import TestCase
import get_assignment

class TestEven(TestCase):
	def test_that_is_even_function_exists(self):
		get_assignment.get_even(3)

	def test_that_even_function_returns_correct_value(self):
		actual = get_assignment.get_even(2)
		expected = True
		self.assertEqual(actual, expected)
		actual = get_assignment.get_even(5)
		expected = False
		self.assertEqual(actual, expected)


	def test_that_is_prime_function_exists(self):
		get_assignment.get_prime(3)

	def test_that_prime_function_returns_correct_value(self):
		actual = get_assignment.get_prime(8)
		expected = False
		self.assertEqual(actual, expected)
		actual = get_assignment.get_prime(5)
		expected = True
		self.assertEqual(actual, expected)


	def test_that_is_subtraction_function_exists(self):
		get_assignment.get_subtract(3,2)

	def test_that_subtraction_function_returns_correct_value(self):
		actual = get_assignment.get_subtract(2,9)
		expected = 7
		self.assertEqual(actual, expected)
		actual = get_assignment.get_subtract(5,2)
		expected = 3
		self.assertEqual(actual, expected)


	def test_that_is_quotient_function_exists(self):
		get_assignment.get_quotient(3,2)

	def test_that_quotient_function_returns_correct_value(self):
		actual = get_assignment.get_quotient(9,2)
		expected = 4.5
		self.assertEqual(actual, expected)
		actual = get_assignment.get_quotient(8,4)
		expected = 2
		self.assertEqual(actual, expected)


	def test_that_is_factor_function_exists(self):
		get_assignment.get_factor(3)

	def test_that_factor_function_returns_correct_value(self):
		actual = get_assignment.get_factor(10)
		expected = 4
		self.assertEqual(actual, expected)
		actual = get_assignment.get_factor(2)
		expected = 2
		self.assertEqual(actual, expected)


	def test_that_is_square_function_exists(self):
		get_assignment.get_square(3)

	def test_that_square_function_returns_correct_value(self):
		actual = get_assignment.get_square(25)
		expected = True
		self.assertEqual(actual, expected)
		actual = get_assignment.get_square(7)
		expected = False
		self.assertEqual(actual, expected)


	def test_that_is_palindrome_function_exists(self):
		get_assignment.get_palindrome(3)

	def test_that_palindrome_function_returns_correct_value(self):
		actual = get_assignment.get_palindrome(25152)
		expected = True
		self.assertEqual(actual, expected)
		actual = get_assignment.get_palindrome(23131)
		expected = False
		self.assertEqual(actual, expected)


	def test_that_is_factorial_function_exists(self):
		get_assignment.get_factorial(3)

	def test_that_factorial_function_returns_correct_value(self):
		actual = get_assignment.get_factorial(5)
		expected = 120
		self.assertEqual(actual, expected)
		actual = get_assignment.get_factorial(10)
		expected = 3628800
		self.assertEqual(actual, expected)


	def test_that_is_raise_function_exists(self):
		get_assignment.get_raise(3)

	def test_that_raise_function_returns_correct_value(self):
		actual = get_assignment.get_raise(5)
		expected = 25
		self.assertEqual(actual, expected)
		actual = get_assignment.get_raise(10)
		expected = 100
		self.assertEqual(actual, expected)

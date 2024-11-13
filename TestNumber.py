from unittest import TestCase
import number

class TestNumber(TestCase):
	def test_multiplication(self):
		number.get_multiplication(3)

	def test_that_cube_function_returns_correct_value(self):
		actual = number.get_multiplication(3)
		expected = 9
		self.assertEqual(actual, expected)
		actual = cube.get_multiplication(10)
		expected = 100
		self.assertEqual(actual, expected)

	def test_that_cube_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, cube.get_cube, "hamid")

	
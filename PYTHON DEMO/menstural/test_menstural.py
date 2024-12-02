from unittest import TestCase
import get_mestural

class TestMesturalCycle(TestCase):
	def test_that_is_next_mestural_cycle_function_exists(self):
		 get_mestural.calculate_next_period_start(3,6)

	def test_that_cycle_function_returns_correct_value(self):
		actual =  get_mestural.calculate_next_period_start(1,20)
		expected = 21
		self.assertEqual(actual, expected)
		actual =  get_mestural.calculate_next_period_start(1,23)
		expected = 24
		self.assertEqual(actual, expected)

	def test_that_it_does_not_accept_string_values(self):
		self.assertRaises(TypeError,  get_mestural.calculate_next_period_start, "hamid")





	def test_that_is_ovulation_day_cycle_function_exists(self):
		 get_mestural.calculate_ovulation_day(3,6)

	def test_that_ovulation_day_function_returns_correct_value(self):
		actual =  get_mestural.calculate_ovulation_day(1,28)
		expected = 15
		self.assertEqual(actual, expected)
		actual =  get_mestural.calculate_ovulation_day(1,16)
		expected = 3
		self.assertEqual(actual, expected)

	def test_that_it_does_not_accept_string_values(self):
		self.assertRaises(TypeError,  get_mestural.calculate_ovulation_day, "hamid")





	def test_that_is_fertile_start_function_exists(self):
		 get_mestural.calculate_fertile_start(3,6)

	def test_that_fertile_start_function_returns_correct_value(self):
		actual =  get_mestural.calculate_fertile_start(1,28)
		expected = 10
		self.assertEqual(actual, expected)
		actual =  get_mestural.calculate_fertile_start(1,20)
		expected = 2
		self.assertEqual(actual, expected)

	def test_that_it_does_not_accept_string_values(self):
		self.assertRaises(TypeError,  get_mestural.calculate_fertile_start, "hamid")






	def test_that_is_fertile_end_function_exists(self):
		 get_mestural.calculate_fertile_end(3,6)

	def test_that_fertile_end_function_returns_correct_value(self):
		actual =  get_mestural.calculate_fertile_end(1,28)
		expected = 16
		self.assertEqual(actual, expected)
		actual =  get_mestural.calculate_fertile_end(1,20)
		expected = 8
		self.assertEqual(actual, expected)

	def test_that_it_does_not_accept_string_values(self):
		self.assertRaises(TypeError,  get_mestural.calculate_fertile_end, "hamid")
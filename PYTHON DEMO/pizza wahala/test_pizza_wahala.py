from unittest import TestCase
import pizza_wahala 

class TestPizzaWahala(TestCase):
	def test_that_calculate_totals_function_exists(self):
		pizza_wahala.get_slices_per_box("hamid")

	def test_that_slice_totals_returns_correct_values(self):
		actual = pizza_wahala.get_slices_per_box("sapa")
		expected = 4
		self.assertEqual(actual, expected)

		actual = pizza_wahala.get_slices_per_box("odogwu")
		expected = 12
		self.assertEqual(actual, expected)

	def test_that_pizza_totals_does_not_accept_integer(self):
		self.assertRaises(TypeError, pizza_wahala.get_slices_per_box, 23)

	def test_that_price_function_exists(self):
		pizza_wahala.get_price_per_box("hamid")

	def test_that_price_returns_correct_values(self):
		actual = pizza_wahala.get_price_per_box("sapa")
		expected = 1500
		self.assertEqual(actual, expected)

		actual = pizza_wahala.get_price_per_box("odogwu")
		expected = 5200
		self.assertEqual(actual, expected)




	def test_that_calculate_boxes_needed_function_exists(self):
		pizza_wahala.calculate_boxes_needed(5,8)

	def test_that_calculate_boxes_needed_returns_correct_values(self):
		actual = pizza_wahala.calculate_boxes_needed(2,6)
		expected = 1
		self.assertEqual(actual, expected)

		actual = pizza_wahala.calculate_boxes_needed(12,12)
		expected = 1
		self.assertEqual(actual, expected)


	def test_that_calculate_leftover_slices_needed_function_exists(self):
		pizza_wahala.calculate_leftover_slices(5,8,3)

	def test_that_calculate_leftover_slices_needed_returns_correct_values(self):
		actual = pizza_wahala.calculate_leftover_slices(2,6,3)
		expected = 16
		self.assertEqual(actual, expected)

		actual = pizza_wahala.calculate_leftover_slices(4,12,2)
		expected = 20
		self.assertEqual(actual, expected)


	def test_that_calculate_total_cost_function_exists(self):
		pizza_wahala.calculate_total_cost(5,8)

	def test_that_calculate_total_cost_returns_correct_values(self):
		actual = pizza_wahala.calculate_total_cost(2,5200)
		expected = 10400
		self.assertEqual(actual, expected)

		actual = pizza_wahala.calculate_total_cost(4,4000)
		expected = 16000
		self.assertEqual(actual, expected)


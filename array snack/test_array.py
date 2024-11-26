from unittest import TestCase
import get_array

class TestWeekendSnack(TestCase):

    def test_that_is_largest_function_exists(self):
        get_array.largest_element([1, 2, 3, 4])

    def test_that_largest_function_returns_correct_value(self):
        actual = get_array.largest_element([1, 2, 3, 4])
        expected = 4
        self.assertEqual(actual, expected)
        actual = get_array.largest_element([5, 6, 7])
        expected = 7
        self.assertEqual(actual, expected)

    def test_that_is_reverse_function_exists(self):
        get_array.reverse_list([1, 2, 3])

    def test_that_reverse_function_returns_correct_value(self):
        actual = get_array.reverse_list([1, 2, 3])
        expected = [3, 2, 1]
        self.assertEqual(actual, expected)
        actual = get_array.reverse_list([4, 5])
        expected = [5, 4]
        self.assertEqual(actual, expected)

    def test_that_is_element_occurs_function_exists(self):
        get_array.element_occurs([1, 2, 3], 2)

    def test_that_element_occurs_function_returns_correct_value(self):
        actual = get_array.element_occurs([1, 2, 3], 2)
        expected = True
        self.assertEqual(actual, expected)
        actual = get_array.element_occurs([1, 2, 3], 4)
        expected = False
        self.assertEqual(actual, expected)

    def test_that_is_odd_positions_function_exists(self):
        get_array.odd_positions([1, 2, 3, 4])

    def test_that_odd_positions_function_returns_correct_value(self):
        actual = get_array.odd_positions([1, 2, 3, 4])
        expected = [1, 3]
        self.assertEqual(actual, expected)

    def test_that_is_even_positions_function_exists(self):
        get_array.even_positions([1, 2, 3, 4])

    def test_that_even_positions_function_returns_correct_value(self):
        actual = get_array.even_positions([1, 2, 3, 4])
        expected = [2, 4]
        self.assertEqual(actual, expected)

    def test_that_is_running_total_function_exists(self):
        get_array.running_total([1, 2, 3])

    def test_that_running_total_function_returns_correct_value(self):
        actual = get_array.running_total([1, 2, 3])
        expected = [1, 3, 6]
        self.assertEqual(actual, expected)

    def test_that_is_palindrome_function_exists(self):
        get_array.is_palindrome("madam")

    def test_that_palindrome_function_returns_correct_value(self):
        actual = get_array.is_palindrome("madam")
        expected = True
        self.assertEqual(actual, expected)
        actual = get_array.is_palindrome("hello")
        expected = False
        self.assertEqual(actual, expected)

    def test_that_is_sum_for_loop_function_exists(self):
        get_array.sum_for_loop([1, 2, 3])

    def test_that_sum_for_loop_function_returns_correct_value(self):
        actual = get_array.sum_for_loop([1, 2, 3])
        expected = 6
        self.assertEqual(actual, expected)

    def test_that_is_sum_while_loop_function_exists(self):
        get_array.sum_while_loop([1, 2, 3])

    def test_that_sum_while_loop_function_returns_correct_value(self):
        actual = get_array.sum_while_loop([1, 2, 3])
        expected = 6
        self.assertEqual(actual, expected)

    def test_that_is_concatenate_lists_function_exists(self):
        get_array.concatenate_lists([1, 2], [3, 4])

    def test_that_concatenate_lists_function_returns_correct_value(self):
        actual = get_array.concatenate_lists([1, 2], [3, 4])
        expected = [1, 2, 3, 4]
        self.assertEqual(actual, expected)

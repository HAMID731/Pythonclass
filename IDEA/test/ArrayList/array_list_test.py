from unittest import TestCase
import get_array_list

class TestArrayList(TestCase):
    def test_that_add_function_exists(self):
        arr_list = get_array_list.ArrayList()
        arr_list.add(5)

    def test_that_add_function_works_correctly(self):
        arr_list = get_array_list.ArrayList()
        arr_list.add(10)
        arr_list.add(20)
        actual = str(arr_list)
        expected = "[10, 20]"
        self.assertEqual(actual, expected)

    def test_that_remove_function_exists(self):
        arr_list = get_array_list.ArrayList()
        arr_list.add(5)
        arr_list.remove(0)

    def test_that_remove_function_works_correctly(self):
        arr_list = get_array_list.ArrayList()
        arr_list.add(10)
        arr_list.add(20)
        arr_list.add(30)
        arr_list.remove(1)
        actual = str(arr_list)
        expected = "[10, 30]"
        self.assertEqual(actual, expected)



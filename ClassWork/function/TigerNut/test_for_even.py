from unittest import TestCase
import question_one

class TestForEvenNumbers(TestCase):
	def test_that_is_even_function_exists(self):
		question_one.get_even([1,2,3,4,5])

	def test_that_even_function_returns_correct_value(self):
		actual = question_one.get_even([1,2,3,4])
		expected = 6
		self.assertEqual(actual, expected)
		actual = question_one.get_even([1,6,3,4])
		expected = 10
		self.assertEqual(actual, expected)

	def test_that_it_does_not_accept_string_values(self):
		self.assertRaises(TypeError, question_one.get_even, "hamid")

class TestForNumberOfVowels(TestCase):
	def test_that_is_vowel_function_exists(self):
		question_one.get_vowel(["aerr"])

	def test_that_vowel_function_returns_correct_value(self):
		actual = question_one.get_vowel(["good"])
		expected = 2
		self.assertEqual(actual, expected)
		actual = question_one.get_vowel(["python"])
		expected = 1
		self.assertEqual(actual, expected)

	def test_that_it_does_not_accept_string_values(self):
		self.assertRaises(TypeError, question_one.get_vowel, 35)

	def test_that_it_can_accept_more_than_one_element(self):
		actual = question_one.get_vowel(["good","python"])
		expected = 3
		self.assertEqual(actual, expected)
		actual = question_one.get_vowel(["python","is","great"])
		expected = 4
		self.assertEqual(actual, expected)

class TestForAnagram(TestCase):
	def test_that_is_anagram_function_exists(self):
		question_one.get_anagram("sdf","nff")

	def test_that_anagram_function_returns_correct_value(self):
		actual = question_one.get_anagram("good","doog")
		expected = True
		self.assertEqual(actual, expected)
		actual = question_one.get_anagram("listen","silent")
		expected = True
		self.assertEqual(actual, expected)
class TestForPrime(TestCase):
	def test_that_is_prime_function_exists(self):
		question_one.get_prime(3)

	def test_that_prime_function_returns_correct_value(self):
		actual = question_one.get_prime(5)
		expected = True
		self.assertEqual(actual, expected)
		actual = question_one.get_prime(6)
		expected = False
		self.assertEqual(actual, expected)

class TestForPalindrome(TestCase):
	def test_that_is_palindrome_function_exists(self):
		question_one.get_palindrome("string")

	def test_that_palindrome_function_returns_correct_value(self):
		actual = question_one.get_palindrome("madam")
		expected = True
		self.assertEqual(actual, expected)
		actual = question_one.get_palindrome("gstt")
		expected = False
		self.assertEqual(actual, expected)

class TestForAverage(TestCase):
	def test_that_is_Average_function_exists(self):
		question_one.get_average([1,2,3,4,5])

	def test_that_palindrome_function_returns_correct_value(self):
		actual = question_one.get_average([1,2,3,4,5])
		expected = 3
		self.assertEqual(actual, expected)
		actual = question_one.get_average([1,1,1,1])
		expected = 1
		self.assertEqual(actual, expected)

class TestForSum(TestCase):
	def test_that_sum_number_return_correct_result(self):
			number = [1,2,3,4,5,6,7,8,9,10]
			actual = question_one.sum_number(number)
			expected = 495
			self.assertEqual(actual,expected)
       

class TestForAdd(TestCase):
    def test_that_is_Add_function_exists(self):
        actual = question_one.get_add([1, 2, 3], [5, 6, 7,-9])
        expected = [-9,1, 2, 3, 5, 6, 7]
        self.assertEqual(actual, expected)

    def test_that_palindrome_function_returns_correct_value(self):
        actual = question_one.get_add([1, 2, 3], [4, 7, 8])
        expected = [1, 2, 3, 4, 7, 8]
        self.assertEqual(actual, expected)

   
class TestForReverse(TestCase):
	def test_that_is_reverse_function_exists(self):
		question_one.get_reverse("Great")

	def test_that_reverse_function_returns_correct_value(self):
		actual = question_one.get_reverse("DIMAH")
		expected = "HAMID"
		self.assertEqual(actual, expected)
		actual = question_one.get_reverse("ENGINEER")
		expected = "REENIGNE"
		self.assertEqual(actual, expected)
class TestForCapitalize(TestCase):
	def test_that_is_capitalize_function_exists(self):
		question_one.get_capitalize_strings(["mango" , "apple" , "bannana"])

	def test_that_capitalize_function_returns_correct_value(self):
		actual = question_one.get_capitalize_strings(["kido" , "kill" , "keren"])
		expected = ["Kido" , "Kill" , "Keren"]
		self.assertEqual(actual, expected)
		

class TestForDuplicate(TestCase):
	def test_that_is_duplicate_function_exists(self):
		question_one.contains_duplicates([1,3,4,5,1,2])

	def test_that_duplicate_function_returns_correct_value(self):
		actual = question_one.contains_duplicates([1,2,3,4,4])
		expected = True
		self.assertEqual(actual, expected)



class TestForSpace(TestCase):
	def test_that_is_space_function_exists(self):
		question_one.remove_spaces("H Y D")

	def test_that_space_function_returns_correct_value(self):
		actual = question_one.remove_spaces("hi how are you")
		expected = "hihowareyou"
		self.assertEqual(actual, expected)



class TestForCommon(TestCase):
	def test_that_is_common_function_exists(self):
		question_one.common_elements([1, 2, 3], [3, 4, 5])

	def test_that_common_function_returns_correct_value(self):
		actual = question_one.common_elements([2, 3, 1], [1, 2, 5])
		expected = [2,1]
		self.assertEqual(actual, expected)




class TestForProductSum(TestCase):
	def test_that_is_product_sum_function_exists(self):
		question_one.get_product_sum([1,2,3,4])

	def test_that_product_sum_function_returns_correct_value(self):
		actual = question_one.get_product_sum([1,2])
		expected = 5
		self.assertEqual(actual, expected)
		actual = question_one.get_product_sum([6,2])
		expected = 40
		self.assertEqual(actual, expected)



class TestForLength(TestCase):
	def test_that_Length_function_exists(self):
		question_one.sort_by_length(["apple", "cashews", "cherry"])

	def test_that_Length_function_returns_correct_value(self):
		actual = question_one.sort_by_length(["carrot", "cucumber", "mango"])
		expected = ["mango", "carrot", "cucumber"]
		self.assertEqual(actual, expected)



class TestForFactoria(TestCase):
	def test_that_factoria_function_exists(self):
		question_one.factorial(4)

	def test_that_factoria_function_returns_correct_value(self):
		actual = question_one.factorial(8)
		expected = 40320
		self.assertEqual(actual, expected)



class TestForDigit(TestCase):
	def test_that_digit_function_exists(self):
		question_one.sum_of_digits(423)

	def test_that_digit_function_returns_correct_value(self):
		actual = question_one.sum_of_digits(12345)
		expected = 15
		self.assertEqual(actual, expected)




class TestForOdds(TestCase):
	def test_that_odds_function_exists(self):
		question_one.get_sum_of_odd_digits(4231)

	def test_that_odds_function_returns_correct_value(self):
		actual = question_one.get_sum_of_odd_digits(11352)
		expected = 10
		self.assertEqual(actual, expected)



class TestForMerge(TestCase):
	def test_that_merge_function_exists(self):
		question_one.merge_lists([1,2,3],[4,5,6])

	def test_that_merge_function_returns_correct_value(self):
		actual = question_one.merge_lists([4,5,-2,6],[6,2,45])
		expected = [-2,2,4,5,6,6,45]
		self.assertEqual(actual, expected)




class TestForAcronym(TestCase):
	def test_that_acronym_function_exists(self):
		question_one.get_acronym("Microsoft Is Across")

	def test_that_acronym_function_returns_correct_value(self):
		actual = question_one.get_acronym("Microsoft Word Office")
		expected = "MWO"
		self.assertEqual(actual, expected)
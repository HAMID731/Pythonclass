def get_even(val:list)->int:
	if type(val) is list:
		sum = 0
		for val in val:
			if val % 2 == 0:
				sum += val
		return sum
	raise TypeError("in valid input")
print(get_even([1,2,3,4,5,6]))




def get_vowel(listName):
	string = ''.join(listName)
	count = 0
	vowels = 'aeiouAEIOU'
	for ch in string:
		if ch in vowels:
			count += 1
	return count

print(get_vowel(["good","python"]))





def get_anagram(s1, s2): 
	if(sorted(s1) == sorted(s2)):
		return True 
	else:
		return False
print(get_anagram("listen","silent"))




def get_prime(n): 
	if n <= 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True
	
print(get_prime(11))




def get_palindrome(string):
	if(string==string[::-1]):  
		return True  
	else:  
		return False  
print(get_palindrome("madam"))




def get_average(a:list)->int:

	avg = sum(a) / len(a)
	return avg
print(get_average([1,5,7,3,2,9]))





def sum_number(number):
	total = 0
	for count in range(len(number)):
		for numbers in number:
			total += numbers
		total -= number[count]
	return total



def get_add(list2 , list1: list):
    list2.extend(list1)
    list2.sort()
    return list2
print(get_add([7 ,8 , 9],[10, 11, 12]))




def get_reverse(stri):
	reversed_string = stri[::-1]
	return reversed_string
print(get_reverse("HAMID"))




def get_capitalize_strings(strings):
    new_list = []
    i = 0
    while i < len(strings):
        new_list.append(strings[i][0].upper() + strings[i][1:])
        i += 1
    return new_list

result = get_capitalize_strings(["apple", "banana", "cherry"])
print(result)





def contains_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False

result = contains_duplicates([1, 2, 3, 4, 5, 2])
print(result)




def remove_spaces(s):
    return ''.join(s.split())

result = remove_spaces("hello world")
print(result)



def common_elements(list1, list2):
    common = []
    for element in list1:
        if element in list2:
            common.append(element)
    return common

result = common_elements([1, 2, 3], [3, 4, 5])
print(result)



def get_product_sum(numbers):
    product = 0
    for num in numbers:
        product += num * num
    return product

result = get_product_sum([1, 2, 3, 4])
print(result)



def sort_by_length(words):
    sorted_words = []
    while words:
        shortest = words[0]
        for word in words:
            if len(word) < len(shortest):
                shortest = word
        sorted_words.append(shortest)
        words.remove(shortest)
    return sorted_words

result = sort_by_length(["apple", "cashews", "cherry"])
print(result)



def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

result = factorial(5)
print(result)


def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

result = sum_of_digits(15324)
print(result)



def get_sum_of_odd_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            total += digit
        n //= 10
    return total

result = get_sum_of_odd_digits(12345)
print(result)



def merge_lists(list1, list2):
    merged = list1 + list2
    merged.sort()
    return merged

result = merge_lists([1, 3, 5], [2, 4, 6])
print(result)



def get_acronym(s):
    words = s.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym

result = get_acronym("Portable Network Graphics")
print(result)


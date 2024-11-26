def get_even(number:list):
	result = list()
	for count in number:
		if count % 2 == 0:
			result.append(True)
		else:
			result.append(False)
	return result
print(get_even([1,2,3,4,5]))

def get_half(my_list:list)->list:
	first_slice = my_list[:1]
	second_slice = my_list[5:]
	result = [first_slice , second_slice]
	return result
print(get_half([1,2,3,4,5,6,7,8,9]))

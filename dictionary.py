def count_frequencies(array):
	frequency_dict = {}
	for element in array:
		if element in frequency_dict:
			frequency_dict[element] += 1
		
array = [2, 2, 1, 3, 5, 5]
output = count_frequencies(array)
print(output)




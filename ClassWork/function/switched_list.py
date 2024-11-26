def get_switched_list(numbers,number:int)->list:
	numbers = [1,2,3,4,5]
	number = 2
	numb=[] 
	lis = []
	for i in numbers :
		lis = i.pop(2)
		i.append(lis)
	return i
print(get_switched_list([1,2,3,4],2))

			
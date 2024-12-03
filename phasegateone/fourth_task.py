import random

number = 0
total = 0

while number <= 9:
	sum = 0
	
	first_random_number = random.randint(1,100)
	second_random_number = random.randint(1,100)

	if first_random_number > second_random_number:
		print(f"{first_random_number}  -  {second_random_number}")
		user_input  = int(input("Enter result: "))		

		subtraction = first_random_number - second_random_number
		if subtraction == user_input :
			sum += 1
			print(" collect! ")
			total = sum
		else :
			sum += 0
			total = sum
			print(" incorrect! ")
		number += 1
			print (total)
	




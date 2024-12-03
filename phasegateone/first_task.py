import random

first_random_number = random.randint(1,100)
print(first_random_number)

second_random_number = random.randint(1,100)
print(second_random_number)

real_sum = second_random_number + first_random_number
user_input  = int(input("Enter result: "))

if user_input == real_sum :
	print("True")
else :
	print("False")
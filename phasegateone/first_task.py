"""
import a class RANDOM

create a variable that gives the  first random number[first_random_number]

create a variable that gives the  second random number[second_random_number]

calculate the total and initialize it to [real_sum]

prompt user to enter his sum 
collect the [user_input]
store as [user_input]

if  [real_sum]==[user_input]
display true

else display false
"""



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
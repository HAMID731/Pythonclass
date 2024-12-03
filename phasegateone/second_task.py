"""
import a class RANDOM

create a variable that gives random number

define a function          [ get_sum_of_each_digit]

using a list comprehention return the sum of number after number iterate through the random number in string

assign the function [ get_sum_of_each_digit] to sum with random_number parameter

display sum

import random

random_number =  random.randint(1,1000)
def get_sum_of_each_digit(random_number) :
	return sum([int(number) for number in str(random_number)])

sum = get_sum_of_each_digit(random_number)
print(f"random number= {random_number}")
print(f" sum= {sum}")
		
	
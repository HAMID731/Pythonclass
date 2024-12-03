"""
import random

initialize number
using while loop allow the question should be ask 10 times i.e while number<=9

initialize a variable sum to zero
generate 2 random number in range 1-100
if first number > second number 
display the quaestion first number - second number
calculate the real result (first number - second number) and store as real result

prompt user to enter answer
collect number
store as user_input 

if real result = user_input
display "correct!"
sum += 1
and assign sum to a variable total

else 
display "incorrect"
"""


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
	




import math
def get_remainder(number):
	result = 0

	if number > 1000 :
		raise ValueError


	if number < 0 :
		raise ValueError

	if number == 0 :
		raise ZeroDivisionError

	if type(number) in [str]:
		raise TypeError	

	if number % 5 == 0:
		result = round(number**(1/2),2)

	elif number % 5 != 0:
		result = number % 5
	

	return result

		
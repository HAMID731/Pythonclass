def get_even(integer:int) -> bool:
	if integer % 2 == 0 :
		return True
	else:
		return False


def get_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

	
def get_subtract(integer: int,integer1: int) -> int:
	if integer > integer1:

		sum = integer - integer1
		
	else:
		sum = integer1 - integer
	return sum


def get_quotient(number1: int,number2: int) -> float:
		if number2 == 0:
			return 0

		sum = 0
		sum = number1 / number2
	
		return sum

def get_factor(num: int) -> int:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count


def get_square(number: int) -> bool:
    if number < 0:
        return False

    sqrt = int(number**0.5)
    
    return sqrt * sqrt == number

def get_palindrome(number: int) -> bool:
    num_str = str(number)

    return num_str == num_str[::-1]



def get_factorial(number: int) -> int:
    if number == 0:
        return 1

    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

def get_raise(num: int)->int:
	sum = num*num
	return sum
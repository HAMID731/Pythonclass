number = int(input("Enter an integer: "))

number1 = number % 100
number2 = number1 /10#second to last
number3 = number1 % 10# last
number4 = number / 1000
number5 = number4 % 10#second
number6 = number4 / 10#first

if number6 == number3 and number5 == number2:
	print("It is a palindrome")
else:
	print("It is not a palindrome")

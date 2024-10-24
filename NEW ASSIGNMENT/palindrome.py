num1=int(input("ENTER A NUMBER"))

first= num1 % 10
last = num1//100

if first==last:
	print("THIS IS A PALINDROME")
if first!=last:
	print("THIS IS NOT A PALINDROME")

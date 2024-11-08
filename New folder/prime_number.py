number = int(input("Enter number: "))

for counter in range(2,number):
	if number % counter == 0 :
		print("It is not  a prime number")
	break

for counter in range(2,number):
	if number % counter != 0:
		print("It is a prime number")
	break
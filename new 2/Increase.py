numberOne = int(input("Enter first number: "))
numberTwo = int(input("Enter second number: "))
numberThree = int(input("Enter third number: "))

if numberOne>numberTwo and numberTwo>numberThree:
	print("They are in decreasing other")

elif numberThree>numberTwo and numberThree>numberOne:
	print("They are in increasing  other")

else :
	print("They are not in order")

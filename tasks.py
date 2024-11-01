number = int(input("ENTER NUMBER"))
sum = 0
remaining = 0
while number>0:
	remaining = number % 10
	sum = sum +remaining
	number = number // 10
	print(sum)
	

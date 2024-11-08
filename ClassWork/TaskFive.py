number = int(input("Enter the number of line: "))

for i in range (number+2):
	for j in range (1,i):
		print(f"{j}",end="")
	print()

for i in range(1,number):
    for j in range(i+2):
        print( j, end="")  
    print()
print()
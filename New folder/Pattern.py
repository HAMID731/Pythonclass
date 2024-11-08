number = int(input("Enter number: "))

for i in range(0,number):
	for j in range(1,i+1):
		print(j,end="")
	print()

for i in range(number,0,-1):
    	for j in range(1,i+1):
        	print( j, end="")  
    	print()
print()

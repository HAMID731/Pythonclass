num = int(input("Enter number: 0"))
count1=0
count2=0

for i in range(0,num):
	if (i % 2) == 0:
		count1 += 1
	else:
		count2 += 1
print(f"the number of even numbers is {count1}")
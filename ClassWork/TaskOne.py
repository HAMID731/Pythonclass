count = 0
counter = 0
for number in range (15):
	number = int(input("Enter student mark"))

	if (number >= 45)  :
		count = count + 1

	elif number < 45 :
		counter = counter + 1


print(f"The number of pass is {count}")
print(f"The number of fail is {counter}")


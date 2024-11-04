print("Please enter 10 numbers:")

largest = -1000000
second_largest = -1000000

for i in range(1, 11):
    number = float(input(f"Enter number {i}: "))

    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print("The largest number is:", largest)
print("The second largest number is:", second_largest)

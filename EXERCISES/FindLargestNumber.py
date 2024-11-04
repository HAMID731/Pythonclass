counter = 0
largest = 0

while counter < 10:
    number = int(input("Enter an integer: "))
    if counter == 0 or number > largest:
        largest = number
    counter += 1

print("The largest number is:", largest)

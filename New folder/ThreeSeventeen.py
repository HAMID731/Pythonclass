largest = 0
second_largest = 0
count = 0

for i in range(10):
    number = float(input(f"Enter number {i + 1}: "))
    count += 1
    
    if count == 1:  
        largest = number
    elif number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print(f"The largest number is {largest}")
print(f"The second largest number is {second_largest}")

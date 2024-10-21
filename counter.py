negative_count = 0
positive_count = 0
zero_count = 0

for i in range(5):
    number = int(input("Enter number: "))

    if number < 0:
        negative_count += 1
    elif number == 0:
        zero_count += 1
    else:
        positive_count += 1

print(f"There are {negative_count} negative numbers.")
print(f"There are {positive_count} positive numbers.")
print(f"There are {zero_count} zeros.")


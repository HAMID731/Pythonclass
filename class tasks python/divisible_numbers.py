lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))

found = False
for i in range(lower, upper + 1):
    if i % 7 == 0 and i % 13 == 0:
        print(f"The first number divisible by both 7 and 13 is: {i}")
        found = True
        break

if not found:
    print("No number divisible by both 7 and 13 was found in the range.")

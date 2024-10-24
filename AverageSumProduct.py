
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


sum = num1 + num2 + num3
average = sum / 3
product = num1 * num2 * num3


smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

print(f"Sum: {sum}")
print(f"Average: {average:.2f}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")

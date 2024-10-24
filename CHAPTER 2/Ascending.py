num1 = float(input("ENTER A NUMBER: "))
num2 = float(input("ENTER A NUMBER: "))
num3 = float(input("ENTER A NUMBER: "))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
middle = (num1 + num2 + num3) - largest - smallest

print(f"Largest number: {largest}")
print(f"Middle number: {middle}")
print(f"Smallest number: {smallest}")







x = int(input("Enter the start of the range: "))
y = int(input("Enter the end of the range: "))
p = int(input("Enter the divisor: "))

result = (y // p) - ((x - 1) // p)
print(f"{result}")

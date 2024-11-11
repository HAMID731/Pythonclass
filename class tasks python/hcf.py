a = int(input("Enter number: "))
b = int(input("Enter number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print(a)

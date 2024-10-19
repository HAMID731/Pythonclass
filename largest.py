num1 =int(input("enter an integer"))
num2 =int(input("enter an integer")) 
num3 =int(input("enter an integer"))


largest = num1
smallest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3

print("Largest:", largest)
print("Smallest:", smallest)


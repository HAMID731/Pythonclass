num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
num4 = int(input("Enter the fourth integer: "))

total_sum = num1 + num2 + num3 + num4
average = total_sum / 4
product = num1 * num2 * num3 * num4
smallest = min(num1, num2, num3, num4)
largest = max(num1, num2, num3, num4)

print("Sum:", total_sum)
print("Average:", average)
print("Product:", product)
print("Smallest:", smallest)
print("Largest:", largest)

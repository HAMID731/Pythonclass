start = int(input("Enter the first integer: "))

end = int(input("Enter the second integer (greater than the first): "))
while end <= start:
    end = int(input("Enter the second integer (greater than the first): "))

sum_even = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        sum_even += i

print(f"Sum of even numbers between {start} and {end} is: {sum_even}")

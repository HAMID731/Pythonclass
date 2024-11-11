number = int(input("Enter a positive integer: "))
sum_divisors = 0
i = 1

while i <= number // 2:
    if number % i == 0:
        sum_divisors += i
    i += 1

if sum_divisors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

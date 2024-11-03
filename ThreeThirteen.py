number = int(input("Enter a five-digit integer: "))
original = number
reverse = 0

first_digit = original // 10000
second_digit = (original // 1000) % 10
third_digit = (original // 100) % 10
fourth_digit = (original // 10) % 10
fifth_digit = original % 10

print(f"Digits: {first_digit}, {second_digit}, {third_digit}, {fourth_digit}, {fifth_digit}")

reverse = fifth_digit * 10000 + fourth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit

if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")

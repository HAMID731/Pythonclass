binary_number = int(input("Enter a binary number: "))
decimal_value = 0
position = 0

while binary_number > 0:
    last_digit = binary_number % 10
    decimal_value += last_digit * (2 ** position)
    binary_number //= 10
    position += 1

print("Decimal equivalent:", decimal_value)

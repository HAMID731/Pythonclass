binary_integer = int(input("Enter a binary integer (only 0s and 1s): "))
decimal_value = 0
positional_value = 1

while binary_integer > 0:
    decimal_value += binary_integer % 10 * positional_value
    binary_integer //= 10
    positional_value *= 2

print("Decimal equivalent:", decimal_value)

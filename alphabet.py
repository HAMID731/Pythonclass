num = int(input("Enter a number: "))

# Print the upper half of the diamond
for i in range(num):
    print(" " * (num - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end="")
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    print()

# Print the lower half of the diamond
for i in range(num - 2, -1, -1):
    print(" " * (num - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end="")
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    print()


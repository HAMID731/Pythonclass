base_length = int(input("Enter the length of the base of the triangle (between 1 and 10): "))

if base_length < 1 or base_length > 10:
    print("Please enter a valid base length between 1 and 10.")
else:
    for i in range(1, base_length + 1):
        for j in range(i):
            print("*", end="")
        print()

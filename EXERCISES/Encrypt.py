number = int(input("Enter a four-digit integer: "))
d0 = (number // 1000 + 7) % 10
d1 = (number // 100 % 10 + 7) % 10
d2 = (number // 10 % 10 + 7) % 10
d3 = (number % 10 + 7) % 10
encrypted_number = d2 * 1000 + d3 * 100 + d0 * 10 + d1
print("Encrypted number:", encrypted_number)

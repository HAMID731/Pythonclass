number = int(input("Enter an integer: "))
original = number
reverse = 0

while number > 0:
    remainder = number % 10  
    reverse = reverse * 10 + remainder  
    number //= 10  

if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")

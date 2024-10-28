while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sum = num1 + num2
        print(f"Sum: {sum}")
        
        repeat = input("Do you want to repeat? (y/n): ").lower()
        if repeat != 'y':
            break

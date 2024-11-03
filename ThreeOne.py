passes = 0
failures = 0

while True:
    value = int(input("Enter 1 for pass, 2 for fail: "))
    if value == 1 or value == 2:
        passes += 1 if value == 1 else 0
        failures += 1 if value == 2 else 0
    else:
        print("Invalid input, please enter 1 or 2.")
    
    if passes + failures == 10:
        break

print("Passes:", passes)
print("Failures:", failures)

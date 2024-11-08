passes = 0  
failures = 0  
total_inputs = 5  

while passes < total_inputs:
    value = input("Enter 1 or 2: ")
    
    
    if value == "1" or value == "2":
        passes += 1
    else:
        print("Invalid input, please enter 1 or 2.")
        failures += 1

print(f"\nTotal passes: {passes}")
print(f"Total failures: {failures}")

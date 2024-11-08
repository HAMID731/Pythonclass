print("Factorials of odd integers from 1 to 9:")
for i in range(1, 10, 2):
    result = 1
    for j in range(1, i + 1):
        result *= j
    print(f"{i}! = {result}")  

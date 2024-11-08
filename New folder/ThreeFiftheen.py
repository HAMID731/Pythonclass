approx = 0
factorial = 1  

for n in range(10):
    if n > 0:
        factorial *= n  
    approx += 1 / factorial
    print(f"e approximation after {n + 1} terms: {approx}")

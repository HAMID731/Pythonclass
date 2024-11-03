x = float(input("Enter the value of x: "))
terms = int(input("Enter the number of terms to approximate e^x: "))

approx_ex = 0
factorial = 1  

for n in range(terms):
    if n > 0:
        factorial *= n  
    approx_ex += (x ** n) / factorial

print(f"Approximation of e^{x} with {terms} terms: {approx_ex}")

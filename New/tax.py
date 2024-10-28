tax_low = 0.15
tax_HIGH = 0.20
income_ceiling = 30000

num_Citizens =int(input("Enter number of citizens"))
while True:
    name = input("Enter citizen's name (or 'exit' to stop): ")
    if name.lower() == 'exit':
        break
earnings = float(input("Enter citizen's earnings: "))

if earnings <= income_ceiling :
	tax = earnings * tax_low
else:
	tax = income_ceiling * tax_low + (earnings - income_ceiling) * tax_HIGH;	
print(f"{name}'s total tax: ${tax:.2f}\n")


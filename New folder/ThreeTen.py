investment = 1000 
rate = 0.07 

for year in range(1, 31):
    investment *= 1 + rate
    print(f"Year {year}: ${investment:.2f}")

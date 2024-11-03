investment = 1000  # Example principal
rate = 0.07  # 7% rate

for year in range(1, 31):
    investment *= 1 + rate
    print(f"Year {year}: ${investment:.2f}")

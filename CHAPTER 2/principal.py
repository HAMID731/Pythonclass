principal = 1000 
rate = 0.07


year1 = 10
year2 =20
year3 =30

for year in range(10,20,30):
    amount = principal * (1 + rate) ** year1
    amount = principal * (1 + rate) ** year2
    amount = principal * (1 + rate) ** year3

    print(f"After {year1} years: ${amount:.2f}")
    print(f"After {year2} years: ${amount:.2f}")
    print(f"After {year3} years: ${amount:.2f}")
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
years = int(input("Enter the number of years: "))
compounds_per_year = int(input("Enter the number of times interest is compounded per year: "))

print(f"{'Year':<5} {'Amount':>10}")
for year in range(1, years + 1):
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * year)
    print(f"{year:<5} {amount:>10.2f}")

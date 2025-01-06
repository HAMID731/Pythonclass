def compound_interest_calculator():
    initial_investment = float(input("Enter the initial investment amount: "))
    monthly_contribution = float(input("Enter the monthly contribution amount (use negative for withdrawals): "))
    years = int(input("Enter the length of time in years: "))
    annual_interest_rate = float(input("Enter the estimated annual interest rate (in %): "))
    compound_frequency = int(input("Enter the compound frequency (e.g., 365 for daily, 12 for monthly): "))

    total_months = years * 12
    interest_rate_per_period = (annual_interest_rate / 100) / compound_frequency
    periods_per_month = compound_frequency / 12

    balance = initial_investment
    for _ in range(total_months):
        balance += monthly_contribution
        balance *= (1 + interest_rate_per_period) ** periods_per_month

    print(f"Final balance after {years} years: ${balance:.2f}")

compound_interest_calculator()

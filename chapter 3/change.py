purchase_price = float(input("Enter purchase price (up to $1.00): "))
change = round(100 - (purchase_price * 100)) 

quarters = change // 25
change %= 25

dimes = change // 10
change %= 10

nickels = change // 5
change %= 5

pennies = change


if quarters > 0:
    print(f"Your change is: {quarters} quarter(s)")
if dimes > 0:
    print(f"Your change is: {dimes} dime(s)")
if nickels > 0:
    print(f"Your change is: {nickels} nickel(s)")
if pennies > 0:
    print(f"Your change is: {pennies} penny(s)")

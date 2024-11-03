purchase_price = float(input("Enter purchase price (up to $1.00): "))
change = round(100 - (purchase_price * 100)) 

quarters = change // 25
change %= 25

dimes = change // 10
change %= 10

nickels = change // 5
change %= 5

pennies = change

print("Your change is:")
if quarters > 0:
    print(f"{quarters} quarter(s)")
if dimes > 0:
    print(f"{dimes} dime(s)")
if nickels > 0:
    print(f"{nickels} nickel(s)")
if pennies > 0:
    print(f"{pennies} penny(s)")

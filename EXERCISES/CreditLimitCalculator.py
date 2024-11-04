number_of_customers = int(input("Enter number of customers: "))

for i in range(number_of_customers):
    print(f"Customer {i + 1}:")
    account_number = int(input("Enter account number: "))
    beginning_balance = int(input("Enter beginning balance: "))
    total_charges = int(input("Enter total charges: "))
    total_credits = int(input("Enter total credits: "))
    credit_limit = int(input("Enter credit limit: "))

    new_balance = beginning_balance + total_charges - total_credits
    print(f"New balance for account {account_number}: {new_balance}")

    if new_balance > credit_limit:
        print("Credit limit exceeded.")
    else:
        print("Credit limit is within range.")
    print() 

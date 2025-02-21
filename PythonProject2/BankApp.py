from Bank import Bank
from Account import Account


def main():
    bank = Bank("First", "Last", "1234")

    while True:
        print("\nWelcome to the Bank App")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Update PIN")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                account_number = int(input("Enter Account Number: "))
                pin = input("Enter PIN: ")
                print(bank.createAccount(account_number, pin))

            case "2":
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter amount to deposit: "))
                print(bank.deposit(amount, account_number))

            case "3":
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter amount to withdraw: "))
                pin = input("Enter your PIN: ")
                print(bank.withdraw(amount, account_number, pin))

            case "4":
                sender = int(input("Enter sender Account Number: "))
                receiver = int(input("Enter receiver Account Number: "))
                amount = float(input("Enter amount to transfer: "))
                pin = input("Enter your PIN: ")
                print(bank.transfer(amount, sender, receiver, pin))

            case "5":
                account_number = int(input("Enter Account Number: "))
                pin = input("Enter your PIN: ")
                print(bank.checkBalance(account_number, pin))

            case "6":
                account_number = int(input("Enter Account Number: "))
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                if account_number in bank.accounts:
                    account = bank.accounts[account_number]
                    print(account.updatePin(old_pin, new_pin))
                else:
                    print("Account not found")

            case "7":
                print("Thank you for using the Bank App!")
                break

            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

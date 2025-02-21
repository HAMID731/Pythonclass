from Account import Account

class Bank:
    def __init__(self, firstName, lastName, password):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.accounts = {}

    def createAccount(self, accountNumber, pin):
        if accountNumber not in self.accounts:
            self.accounts[accountNumber] = Account(accountNumber, self, pin)
            return f"ACCOUNT CREATED SUCCESSFULLY. this is your account number: {accountNumber}"
        else:
            return "ACCOUNT CREATION FAILED (account number already exists)"

    def deposit(self, amount, accountNumber):
        if amount > 0:
            if accountNumber in self.accounts:
                self.accounts[accountNumber].balance += amount
                return "DEPOSITED SUCCESSFULLY"
            else:
                return "DEPOSIT FAILED (account not found)"
        else:
            return "DEPOSIT FAILED (amount cannot be negative)"

    def withdraw(self, amount, accountNumber, password):
        if self.password == password:
            if accountNumber in self.accounts:
                return self.accounts[accountNumber].withdraw(amount, self.accounts[accountNumber].pin)
            else:
                return "WITHDRAWAL FAILED (account not found)"
        else:
            return "WITHDRAWAL FAILED (incorrect password)"

    def checkBalance(self, accountNumber, pin):
        if accountNumber in self.accounts:
            account = self.accounts[accountNumber]
            if account.pin == pin:
                return account.checkBalance()
            else:
                return "BALANCE CHECK FAILED (incorrect PIN)"
        else:
            return "BALANCE CHECK FAILED (account not found)"

    def transfer(self, amount, sender, receiver, pin):
        if sender in self.accounts and receiver in self.accounts:
            withdrawalResult = self.accounts[sender].withdraw(amount, pin)
            if "SUCCESSFUL" in withdrawalResult:
                self.accounts[receiver].balance += amount
                return "TRANSFER SUCCESSFUL"
            else:
                return withdrawalResult
        else:
            return "TRANSFER FAILED (account not found)"

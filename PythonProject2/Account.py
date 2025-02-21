class Account:
    def __init__(self, accountNumber, bank, pin):
        self.accountNumber = accountNumber
        self.bank = bank
        self.pin = pin
        self.balance = 0

    def withdraw(self, amount, pin):
        if self.pin == pin:
            if self.balance >= amount:
                self.balance -= amount
                return "WITHDRAWAL SUCCESSFUL"
            else:
                return "WITHDRAWAL FAILED (insufficient funds)"
        else:
            return "WITHDRAWAL FAILED (incorrect PIN)"

    def checkBalance(self):
        return f"BALANCE: {self.balance}"

    def updatePin(self, oldPin, newPin):
        if self.pin == oldPin:
            self.pin = newPin
            return "PIN UPDATED SUCCESSFULLY"
        else:
            return "PIN UPDATE FAILED (incorrect old PIN)"

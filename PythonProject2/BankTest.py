from unittest import TestCase
from Bank import Bank

class TestBank(TestCase):

    def setUp(self):
        self.bank = Bank("First", "Last", "1234")
        self.pin = "1234"
        self.account_number = 1001

    def test_create_account(self):
        result = self.bank.createAccount(self.account_number, self.pin)
        self.assertIn("ACCOUNT CREATED SUCCESSFULLY", result)

    def test_create_account_failure(self):
        self.bank.createAccount(self.account_number, self.pin)
        result = self.bank.createAccount(self.account_number, self.pin)
        self.assertEqual(result, "ACCOUNT CREATION FAILED (account number already exists)")

    def test_deposit_success(self):
        self.bank.createAccount(self.account_number, self.pin)
        result = self.bank.deposit(100, self.account_number)
        self.assertEqual(result, "DEPOSITED SUCCESSFULLY")

    def test_deposit_failure_negative_amount(self):
        self.bank.createAccount(self.account_number, self.pin)
        result = self.bank.deposit(-50, self.account_number)
        self.assertEqual(result, "DEPOSIT FAILED (amount cannot be negative)")

    def test_deposit_failure_account_not_found(self):
        result = self.bank.deposit(100, 9999)
        self.assertEqual(result, "DEPOSIT FAILED (account not found)")

    def test_withdraw_success(self):
        self.bank.createAccount(self.account_number, self.pin)
        self.bank.deposit(100, self.account_number)
        result = self.bank.withdraw(50, self.account_number, self.pin)
        self.assertIn("WITHDRAWAL SUCCESSFUL", result)

    def test_withdraw_failure_incorrect_password(self):
        self.bank.createAccount(self.account_number, self.pin)
        result = self.bank.withdraw(50, self.account_number, "wrongpassword")
        self.assertEqual(result, "WITHDRAWAL FAILED (incorrect password)")

    def test_transfer_success(self):
        account_number2 = 1002
        self.bank.createAccount(self.account_number, self.pin)
        self.bank.createAccount(account_number2, self.pin)
        self.bank.deposit(100, self.account_number)
        result = self.bank.transfer(50, self.account_number, account_number2, self.pin)
        self.assertEqual(result, "TRANSFER SUCCESSFUL")

    def test_transfer_failure_incorrect_password(self):
        account_number2 = 1002
        self.bank.createAccount(self.account_number, self.pin)
        self.bank.createAccount(account_number2, self.pin)
        self.bank.deposit(100, self.account_number)
        result = self.bank.transfer(50, self.account_number, account_number2, "wrongpassword")
        self.assertEqual(result, "TRANSFER FAILED (incorrect password)")

    def test_check_balance_success(self):
        self.bank.createAccount(self.account_number, self.pin)
        self.bank.deposit(100, self.account_number)
        result = self.bank.checkBalance(self.account_number, self.pin)
        self.assertIn("BALANCE:", result)

    def test_check_balance_failure_incorrect_password(self):
        self.bank.createAccount(self.account_number, self.pin)
        result = self.bank.checkBalance(self.account_number, "wrongpassword")
        self.assertEqual(result, "BALANCE CHECK FAILED (incorrect password)")

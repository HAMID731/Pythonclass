from unittest import TestCase
from Account import Account
from Bank import Bank

class TestAccount(TestCase):

    def setUp(self):
        self.bank = Bank("First", "Last", "1234")
        self.account = Account(1001, self.bank, "1234")

    def test_withdraw_success(self):
        self.account.balance = 100
        result = self.account.withdraw(50, "1234")
        self.assertEqual(result, "WITHDRAWAL SUCCESSFUL")
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_failure_incorrect_pin(self):
        self.account.balance = 100
        result = self.account.withdraw(50, "wrongpin")
        self.assertEqual(result, "WITHDRAWAL FAILED (incorrect PIN)")
        self.assertEqual(self.account.balance, 100)

    def test_withdraw_failure_insufficient_funds(self):
        self.account.balance = 50
        result = self.account.withdraw(100, "1234")
        self.assertEqual(result, "WITHDRAWAL FAILED (insufficient funds)")
        self.assertEqual(self.account.balance, 50)

    def test_check_balance(self):
        self.account.balance = 100
        result = self.account.checkBalance()
        self.assertEqual(result, "BALANCE: 100")

    def test_update_pin_success(self):
        result = self.account.updatePin("1234", "5678")
        self.assertEqual(result, "PIN UPDATED SUCCESSFULLY")
        self.assertEqual(self.account.pin, "5678")

    def test_update_pin_failure_incorrect_old_pin(self):
        result = self.account.updatePin("wrongpin", "5678")
        self.assertEqual(result, "PIN UPDATE FAILED (incorrect old PIN)")
        self.assertEqual(self.account.pin, "1234")

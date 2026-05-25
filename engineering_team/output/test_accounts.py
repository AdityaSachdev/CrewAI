import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account("test_user", 1000.0)

    def test_initialization(self):
        self.assertEqual(self.account.username, "test_user")
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.holdings, {})
        self.assertEqual(self.account.transactions, [])
    
    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500.0)

    def test_deposit_invalid_amount(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100)
        self.assertEqual(str(context.exception), "Deposit amount must be greater than 0.")

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800.0)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(1500)
        self.assertEqual(str(context.exception), "Insufficient funds for withdrawal.")

    def test_buy_share(self):
        self.account.buy_share("AAPL", 2)
        self.assertEqual(self.account.balance, 700.0)
        self.assertEqual(self.account.holdings, {"AAPL": 2})
        self.assertEqual(len(self.account.transactions), 1)

    def test_buy_share_invalid_quantity(self):
        with self.assertRaises(ValueError) as context:
            self.account.buy_share("AAPL", 0)
        self.assertEqual(str(context.exception), "Quantity must be greater than 0.")

    def test_buy_share_insufficient_funds(self):
        with self.assertRaises(ValueError) as context:
            self.account.buy_share("GOOGL", 1)
        self.assertEqual(str(context.exception), "Insufficient funds to buy shares.")

    def test_sell_share(self):
        self.account.buy_share("AAPL", 2)
        self.account.sell_share("AAPL", 1)
        self.assertEqual(self.account.balance, 850.0)
        self.assertEqual(self.account.holdings, {"AAPL": 1})
        self.assertEqual(len(self.account.transactions), 2)

    def test_sell_share_insufficient_quantity(self):
        self.account.buy_share("AAPL", 2)
        with self.assertRaises(ValueError) as context:
            self.account.sell_share("AAPL", 3)
        self.assertEqual(str(context.exception), "Insufficient shares to sell.")

    def test_get_total_portfolio_value(self):
        self.account.deposit(500)
        self.account.buy_share("AAPL", 2)
        self.assertEqual(self.account.get_total_portfolio_value(), 700.0 + 300.0)  # 2 shares of AAPL

    def test_get_profit_or_loss(self):
        self.account.deposit(500)
        self.account.buy_share("AAPL", 2)
        self.assertEqual(self.account.get_profit_or_loss(), 0.0)

    def test_get_holdings(self):
        self.account.buy_share("AAPL", 2)
        self.assertEqual(self.account.get_holdings(), {"AAPL": 2})

    def test_get_transactions(self):
        self.account.deposit(500)
        self.account.buy_share("AAPL", 2)
        self.account.sell_share("AAPL", 1)
        self.assertEqual(len(self.account.get_transactions()), 3)

if __name__ == "__main__":
    unittest.main()
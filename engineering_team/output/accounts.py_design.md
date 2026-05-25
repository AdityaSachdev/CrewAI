```markdown
# Design Document for Account Management System

## Module: accounts.py

This module implements a simple account management system for a trading simulation platform. The key class provided in this module is the `Account` class, which allows users to manage their trading activities, including account creation, fund management, share transactions, and portfolio reporting.

### Classes

#### 1. Account

The `Account` class encapsulates all functionalities related to account management and trades.

##### Attributes:
- `username` (str): The username of the account holder.
- `balance` (float): The current balance of the user's account.
- `holdings` (dict): A dictionary where keys are share symbols and values are the quantities of shares owned.
- `transactions` (list): A list to keep track of all transactions made by the user. Each transaction is a dictionary containing `symbol`, `quantity`, `transaction_type`, and `price`.
- `initial_deposit` (float): The initial deposit made by the user.

##### Methods:

- `__init__(self, username: str, initial_deposit: float) -> None`
    - Initializes a new account with a specified username and initial deposit.
  
- `deposit(self, amount: float) -> None`
    - Adds funds to the account balance.
    - Args:
        - `amount` (float): The amount to deposit which must be greater than 0.

- `withdraw(self, amount: float) -> None`
    - Withdraws funds from the account balance.
    - Args:
        - `amount` (float): The amount to withdraw. Must not exceed the current balance.
  
- `buy_share(self, symbol: str, quantity: int) -> None`
    - Records the purchase of shares and updates the account balance and holdings.
    - Args:
        - `symbol` (str): The stock symbol for the share to buy.
        - `quantity` (int): The number of shares to buy.
    - Raises an exception if the user cannot afford the shares.

- `sell_share(self, symbol: str, quantity: int) -> None`
    - Records the sale of shares, updating the account balance and holdings.
    - Args:
        - `symbol` (str): The stock symbol for the share to sell.
        - `quantity` (int): The number of shares to sell.
    - Raises an exception if the user does not own enough shares.

- `get_total_portfolio_value(self) -> float`
    - Calculates the total value of the user's portfolio based on current share prices.
    - Returns:
        - `float`: The total market value of all shares held.

- `get_profit_or_loss(self) -> float`
    - Calculates the profit or loss from the initial deposit based on the current account balance.
    - Returns:
        - `float`: The profit or loss.

- `get_holdings(self) -> dict`
    - Returns the current holdings of the user.
    - Returns:
        - `dict`: A dictionary of shares and their quantities.

- `get_transactions(self) -> list`
    - Returns a list of all transactions made by the user.
    - Returns:
        - `list`: A list of transaction dictionaries.

### Helper Functions

#### 1. get_share_price(symbol: str) -> float

This function is responsible for returning the current price of a share based on its symbol. 

##### Implementation:
- A simple fixed price return for demonstration purposes can be as follows:
    - If `symbol` is "AAPL", return 150.00
    - If `symbol` is "TSLA", return 700.00
    - If `symbol` is "GOOGL", return 2800.00
    - Otherwise, raise a `ValueError`.

### Usage Example

```python
account = Account("john_doe", initial_deposit=1000.00)
account.deposit(500.00)
account.buy_share("AAPL", 2)
portfolio_value = account.get_total_portfolio_value()
profit_loss = account.get_profit_or_loss()
holdings = account.get_holdings()
transactions = account.get_transactions()
```
```

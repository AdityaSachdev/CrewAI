class Account:
    def __init__(self, username: str, initial_deposit: float) -> None:
        self.username = username
        self.balance = initial_deposit
        self.holdings = {}
        self.transactions = []
        self.initial_deposit = initial_deposit

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount

    def buy_share(self, symbol: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy shares.")
        
        self.balance -= total_cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity

        self.transactions.append({
            'symbol': symbol,
            'quantity': quantity,
            'transaction_type': 'buy',
            'price': share_price
        })

    def sell_share(self, symbol: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Insufficient shares to sell.")
        
        share_price = get_share_price(symbol)
        total_revenue = share_price * quantity
        self.balance += total_revenue
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]

        self.transactions.append({
            'symbol': symbol,
            'quantity': quantity,
            'transaction_type': 'sell',
            'price': share_price
        })

    def get_total_portfolio_value(self) -> float:
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def get_profit_or_loss(self) -> float:
        current_value = self.get_total_portfolio_value()
        return current_value - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings

    def get_transactions(self) -> list:
        return self.transactions

def get_share_price(symbol: str) -> float:
    if symbol == "AAPL":
        return 150.00
    elif symbol == "TSLA":
        return 700.00
    elif symbol == "GOOGL":
        return 2800.00
    else:
        raise ValueError(f"Unknown share symbol: {symbol}")
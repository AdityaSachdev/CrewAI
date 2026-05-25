
import gradio as gr

# Assuming the Account class and get_share_price function are already defined as provided.
class Account:
    def __init__(self, username: str, initial_deposit: float):
        self.username = username
        self.balance = initial_deposit
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < 0:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: ${amount:.2f}")

    def buy_shares(self, symbol: str, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        price_per_share = get_share_price(symbol)
        total_cost = price_per_share * quantity
        
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to buy shares.")
        
        self.balance -= total_cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        
        self.transactions.append(f"Bought {quantity} shares of {symbol} at ${price_per_share:.2f} each")

    def sell_shares(self, symbol: str, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Insufficient shares to sell.")

        price_per_share = get_share_price(symbol)
        total_revenue = price_per_share * quantity
        
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        
        self.balance += total_revenue
        self.transactions.append(f"Sold {quantity} shares of {symbol} at ${price_per_share:.2f} each")

    def calculate_portfolio_value(self) -> float:
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self) -> float:
        initial_value = sum(get_share_price(symbol) * quantity for symbol, quantity in self.holdings.items()) + self.balance
        return initial_value - self.balance

    def report_holdings(self):
        return self.holdings

    def report_profit_loss(self) -> float:
        return self.calculate_profit_loss()

    def list_transactions(self):
        return self.transactions

def get_share_price(symbol: str) -> float:
    prices = {
        'AAPL': 150.00,
        'TSLA': 700.00,
        'GOOGL': 2800.00
    }
    return prices.get(symbol, 0.0)

# Gradio Interface
def initialize_account(username, initial_deposit):
    account = Account(username, float(initial_deposit))
    return f"Account created for {username} with an initial deposit of ${initial_deposit:.2f}."

def deposit_funds(account, amount):
    account.deposit(float(amount))
    return f"Deposited: ${amount:.2f}. Current balance: ${account.balance:.2f}."

def withdraw_funds(account, amount):
    account.withdraw(float(amount))
    return f"Withdrew: ${amount:.2f}. Current balance: ${account.balance:.2f}."

def buy_stock(account, symbol, quantity):
    account.buy_shares(symbol, int(quantity))
    return f"Bought {quantity} shares of {symbol}. Current balance: ${account.balance:.2f}."

def sell_stock(account, symbol, quantity):
    account.sell_shares(symbol, int(quantity))
    return f"Sold {quantity} shares of {symbol}. Current balance: ${account.balance:.2f}."

def portfolio_value(account):
    total_value = account.calculate_portfolio_value()
    return f"Total portfolio value: ${total_value:.2f}."

def profit_loss(account):
    pl = account.calculate_profit_loss()
    return f"Profit/Loss: ${pl:.2f}."

def holdings(account):
    return account.report_holdings()

def transactions(account):
    return account.list_transactions()

# Gradio UI Layout
with gr.Blocks() as app:
    gr.Markdown("### Account Management System")
    username = gr.Textbox(label="Username")
    initial_deposit = gr.Number(label="Initial Deposit", precision=2)
    
    create_account_btn = gr.Button("Create Account")
    account_msg = gr.Output()

    create_account_btn.click(initialize_account, inputs=[username, initial_deposit], outputs=account_msg)

    with gr.Row():
        deposit_amount = gr.Number(label="Deposit Amount", precision=2)
        deposit_btn = gr.Button("Deposit")
        deposit_msg = gr.Output()

        deposit_btn.click(deposit_funds, inputs=[account_msg, deposit_amount], outputs=deposit_msg)

    with gr.Row():
        withdraw_amount = gr.Number(label="Withdrawal Amount", precision=2)
        withdraw_btn = gr.Button("Withdraw")
        withdraw_msg = gr.Output()

        withdraw_btn.click(withdraw_funds, inputs=[account_msg, withdraw_amount], outputs=withdraw_msg)

    with gr.Row():
        stock_symbol = gr.Textbox(label="Stock Symbol")
        buy_quantity = gr.Number(label="Buy Quantity", precision=0)
        buy_btn = gr.Button("Buy Shares")
        buy_msg = gr.Output()

        buy_btn.click(buy_stock, inputs=[account_msg, stock_symbol, buy_quantity], outputs=buy_msg)

    with gr.Row():
        sell_quantity = gr.Number(label="Sell Quantity", precision=0)
        sell_btn = gr.Button("Sell Shares")
        sell_msg = gr.Output()

        sell_btn.click(sell_stock, inputs=[account_msg, stock_symbol, sell_quantity], outputs=sell_msg)

    with gr.Row():
        portfolio_value_btn = gr.Button("View Portfolio Value")
        portfolio_value_msg = gr.Output()

        portfolio_value_btn.click(portfolio_value, inputs=[account_msg], outputs=portfolio_value_msg)

    with gr.Row():
        profit_loss_btn = gr.Button("View Profit/Loss")
        profit_loss_msg = gr.Output()

        profit_loss_btn.click(profit_loss, inputs=[account_msg], outputs=profit_loss_msg)

    with gr.Row():
        holdings_btn = gr.Button("View Holdings")
        holdings_msg = gr.Output()

        holdings_btn.click(holdings, inputs=[account_msg], outputs=holdings_msg)

    with gr.Row():
        transactions_btn = gr.Button("View Transactions")
        transactions_msg = gr.Output()

        transactions_btn.click(transactions, inputs=[account_msg], outputs=transactions_msg)

# Launch the Gradio app
app.launch()
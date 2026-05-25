import gradio as gr
from accounts import Account, get_share_price

def create_account(username, initial_deposit):
    global account
    try:
        account = Account(username, initial_deposit)
        return "Account created successfully."
    except Exception as e:
        return str(e)

def deposit_funds(amount):
    try:
        account.deposit(amount)
        return f"Deposited ${amount:.2f}. Current balance is ${account.balance:.2f}."
    except Exception as e:
        return str(e)

def withdraw_funds(amount):
    try:
        account.withdraw(amount)
        return f"Withdrew ${amount:.2f}. Current balance is ${account.balance:.2f}."
    except Exception as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        account.buy_share(symbol, quantity)
        return f"Bought {quantity} shares of {symbol}."
    except Exception as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        account.sell_share(symbol, quantity)
        return f"Sold {quantity} shares of {symbol}."
    except Exception as e:
        return str(e)

def check_portfolio_value():
    value = account.get_total_portfolio_value()
    return f"Total portfolio value: ${value:.2f}"

def check_profit_loss():
    profit_or_loss = account.get_profit_or_loss()
    return f"Profit/Loss: ${profit_or_loss:.2f}"

def view_holdings():
    holdings = account.get_holdings()
    return f"Holdings: {holdings}"

def view_transactions():
    transactions = account.get_transactions()
    return f"Transactions: {transactions}"

with gr.Blocks() as demo:
    gr.Markdown("## Trading Simulation Platform")

    with gr.Tab("Account"):
        username_input = gr.Textbox(label="Username")
        initial_deposit_input = gr.Number(label="Initial Deposit", value=1000.0)
        account_create_button = gr.Button("Create Account")
        account_create_output = gr.Textbox()

        account_create_button.click(create_account, [username_input, initial_deposit_input], account_create_output)

        deposit_input = gr.Number(label="Deposit Amount")
        deposit_button = gr.Button("Deposit")
        deposit_output = gr.Textbox()

        deposit_button.click(deposit_funds, [deposit_input], deposit_output)

        withdraw_input = gr.Number(label="Withdraw Amount")
        withdraw_button = gr.Button("Withdraw")
        withdraw_output = gr.Textbox()

        withdraw_button.click(withdraw_funds, [withdraw_input], withdraw_output)

    with gr.Tab("Trading"):
        share_symbol_input = gr.Dropdown(["AAPL", "TSLA", "GOOGL"], label="Share Symbol")
        share_quantity_input = gr.Number(label="Quantity", value=1)

        buy_button = gr.Button("Buy Shares")
        buy_output = gr.Textbox()

        buy_button.click(buy_shares, [share_symbol_input, share_quantity_input], buy_output)

        sell_button = gr.Button("Sell Shares")
        sell_output = gr.Textbox()

        sell_button.click(sell_shares, [share_symbol_input, share_quantity_input], sell_output)

    with gr.Tab("Portfolio"):
        portfolio_value_button = gr.Button("Check Portfolio Value")
        portfolio_value_output = gr.Textbox()

        portfolio_value_button.click(check_portfolio_value, [], portfolio_value_output)

        profit_loss_button = gr.Button("Check Profit/Loss")
        profit_loss_output = gr.Textbox()

        profit_loss_button.click(check_profit_loss, [], profit_loss_output)

        holdings_button = gr.Button("View Holdings")
        holdings_output = gr.Textbox()

        holdings_button.click(view_holdings, [], holdings_output)

        transactions_button = gr.Button("View Transactions")
        transactions_output = gr.Textbox()

        transactions_button.click(view_transactions, [], transactions_output)

if __name__ == "__main__":
    demo.launch()
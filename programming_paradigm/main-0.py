# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Initializing with a default balance of $100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and optional amount
    command_input = sys.argv[1]
    if ":" in command_input:
        command, amount_str = command_input.split(":", 1)
        try:
            amount = float(amount_str)
        except ValueError:
            print("Invalid amount. Please provide a numeric value.")
            sys.exit(1)
    else:
        command = command_input
        amount = None

    # Execute the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()

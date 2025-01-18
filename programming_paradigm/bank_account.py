# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the BankAccount with an optional starting balance."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds are available."""
        if amount > self.__account_balance:
            return False
        elif amount > 0:
            self.__account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

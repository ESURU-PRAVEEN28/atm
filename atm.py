import tkinter as tk
from tkinter import messagebox

# Mock database
users = {
    "1234": {"pin": "1111", "balance": 5000},
    "5678": {"pin": "2222", "balance": 3000},
}

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM")

        self.create_widgets()

    def create_widgets(self):
        # Card Number
        self.card_label = tk.Label(self.root, text="Card Number:")
        self.card_label.pack()
        self.card_entry = tk.Entry(self.root)
        self.card_entry.pack()

        # PIN
        self.pin_label = tk.Label(self.root, text="PIN:")
        self.pin_label.pack()
        self.pin_entry = tk.Entry(self.root, show='*')
        self.pin_entry.pack()

        # Buttons
        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

        self.balance_button = tk.Button(self.root, text="Check Balance", command=self.check_balance, state=tk.DISABLED)
        self.balance_button.pack()

        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw, state=tk.DISABLED)
        self.withdraw_button.pack()

        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit, state=tk.DISABLED)
        self.deposit_button.pack()

        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout, state=tk.DISABLED)
        self.logout_button.pack()

    def login(self):
        card_number = self.card_entry.get()
        pin = self.pin_entry.get()
        if card_number in users and users[card_number]["pin"] == pin:
            self.current_user = card_number
            messagebox.showinfo("Login", "Login Successful!")
            self.balance_button.config(state=tk.NORMAL)
            self.withdraw_button.config(state=tk.NORMAL)
            self.deposit_button.config(state=tk.NORMAL)
            self.logout_button.config(state=tk.NORMAL)
            self.login_button.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Login", "Invalid card number or PIN")

    def check_balance(self):
        balance = users[self.current_user]["balance"]
        messagebox.showinfo("Balance", f"Your balance is: ${balance}")

    def withdraw(self):
        amount = self.prompt_amount("Withdraw")
        if amount is not None:
            if amount <= users[self.current_user]["balance"]:
                users[self.current_user]["balance"] -= amount
                messagebox.showinfo("Withdraw", f"Withdrawn: ${amount}")
            else:
                messagebox.showerror("Withdraw", "Insufficient balance")

    def deposit(self):
        amount = self.prompt_amount("Deposit")
        if amount is not None:
            users[self.current_user]["balance"] += amount
            messagebox.showinfo("Deposit", f"Deposited: ${amount}")

    def logout(self):
        self.current_user = None
        self.balance_button.config(state=tk.DISABLED)
        self.withdraw_button.config(state=tk.DISABLED)
        self.deposit_button.config(state=tk.DISABLED)
        self.logout_button.config(state=tk.DISABLED)
        self.login_button.config(state=tk.NORMAL)
        self.card_entry.delete(0, tk.END)
        self.pin_entry.delete(0, tk.END)
        messagebox.showinfo("Logout", "Logged out successfully")

    def prompt_amount(self, action):
        amount = tk.simpledialog.askinteger(action, f"Enter amount to {action.lower()}:")
        if amount is None or amount <= 0:
            messagebox.showerror(action, "Invalid amount")
            return None
        return amount

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()

import tkinter as tk
from Function import *

root = tk.Tk()
root.title("Banking App")
root.geometry("400x500")

current_user = None

# function to clear the window
def clear():
    for widget in root.winfo_children():
        widget.destroy()

#login UI
def login_ui():
    clear()

    tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Account Number").pack()
    acc_entry = tk.Entry(root)
    acc_entry.pack()

    tk.Label(root, text="PIN").pack()
    pin_entry = tk.Entry(root, show="*")
    pin_entry.pack()

    result = tk.Label(root, text="")
    result.pack()

    def handle_login():
        global current_user
        user = login(acc_entry.get(), pin_entry.get())

        if user:
            current_user = user
            if user["role"] == "admin":
                admin_ui()
            else:
                customer_ui()
        else:
            result.config(text="Invalid login")

    tk.Button(root, text="Login", command=handle_login).pack(pady=10)

#customer UI
def customer_ui():
    clear()

    tk.Label(root, text="Customer Menu", font=("Arial", 16)).pack(pady=10)

    result = tk.Label(root, text="")
    result.pack()

    def show_balance_ui():
        bal = check_balance(current_user["account_number"])
        result.config(text=f"Balance: ${bal}")

    def deposit_ui():
        amount = float(amount_entry.get())
        deposit(current_user["account_number"], amount)
        result.config(text="Deposited")

    def withdraw_ui():
        amount = float(amount_entry.get())
        success = withdraw(current_user["account_number"], amount)

        if success:
            result.config(text="Withdrawn")
        else:
            result.config(text="Not enough money")

    tk.Label(root, text="Amount").pack()
    amount_entry = tk.Entry(root)
    amount_entry.pack()

    tk.Button(root, text="Check Balance", command=show_balance_ui).pack(pady=5)
    tk.Button(root, text="Deposit", command=deposit_ui).pack(pady=5)
    tk.Button(root, text="Withdraw", command=withdraw_ui).pack(pady=5)

#admin UI
def admin_ui():
    clear()

    tk.Label(root, text="Admin Menu", font=("Arial", 16)).pack(pady=10)

    result = tk.Label(root, text="")
    result.pack()

    tk.Label(root, text="Account Number").pack()
    acc_entry = tk.Entry(root)
    acc_entry.pack()

    tk.Label(root, text="PIN").pack()
    pin_entry = tk.Entry(root)
    pin_entry.pack()

    tk.Label(root, text="Balance").pack()
    balance_entry = tk.Entry(root)
    balance_entry.pack()

    def create_ui():
        create_account(acc_entry.get(), pin_entry.get(), float(balance_entry.get()))
        result.config(text="Account created")

    def delete_ui():
        delete_account(acc_entry.get())
        result.config(text="Account deleted")

    def modify_ui():
        modify_pin(acc_entry.get(), pin_entry.get())
        result.config(text="PIN updated")

    tk.Button(root, text="Create Account", command=create_ui).pack(pady=5)
    tk.Button(root, text="Delete Account", command=delete_ui).pack(pady=5)
    tk.Button(root, text="Modify PIN", command=modify_ui).pack(pady=5)

#start the app
def start_app():
    login_ui()
    root.mainloop()
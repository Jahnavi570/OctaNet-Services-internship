import time
from datetime import datetime

# Initialize variables
balance = 5000
transaction_history = []

# Function to display current date and time
def display_datetime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Date and Time =", dt_string)

# Function to display transaction history
def display_transaction_history():
    print("\n--- Transaction History ---")
    for transaction in transaction_history:
        print(transaction)
    print("--------------------------\n")

# Function for withdrawing money
def withdraw_money(amount):
    global balance
    if amount > 0 and balance >= amount:
        balance -= amount
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        transaction_history.append(f"Withdraw: ${amount}, Date: {dt_string}, Balance: ${balance}")
        print(f"\n${amount} withdrawn successfully.")
        print(f"Current Balance: ${balance}")
    else:
        print("\nInsufficient funds or invalid amount.")

# Function for depositing money
def deposit_money(amount):
    global balance
    if amount > 0:
        balance += amount
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        transaction_history.append(f"Deposit: ${amount}, Date: {dt_string}, Balance: ${balance}")
        print(f"\n${amount} deposited successfully.")
        print(f"Current Balance: ${balance}")
    else:
        print("\nInvalid amount.")

# Function for transferring money
def transfer_money(amount):
    global balance
    if amount > balance:
        print("Insufficient balance to transfer.")
    else:
        balance -= amount
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        transaction_history.append(f"Transfer: ${amount}, Date: {dt_string}, Balance: ${balance}")
        print(f"\n${amount} transferred successfully.")
        print(f"Current Balance: ${balance}")

# Main function to run ATM simulation
def main():
    display_datetime()
    print("Welcome to the ATM!")
    print("Please insert your card...\n")
    time.sleep(2)  # Simulating card insertion delay
    
    # Request PIN from user
    print("Enter your PIN:")
    password = 1234  # Replace with your actual ATM PIN
    pin = int(input())

    # Check if PIN is correct
    if pin == password:
        while True:
            print("""
            1. Transaction History
            2. Withdraw
            3. Deposit
            4. Transfer
            5. Quit
            """)

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if choice == 1:
                display_transaction_history()
            
            elif choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                withdraw_money(amount)
            
            elif choice == 3:
                amount = float(input("Enter amount to deposit: "))
                deposit_money(amount)
            
            elif choice == 4:
                amount = float(input("Enter amount to transfer: "))
                transfer_money(amount)
            
            elif choice == 5:
                print("Thank you for using the ATM. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
    else:
        print("Invalid PIN. Access denied.")

if _name_ == "_main_":
    main()

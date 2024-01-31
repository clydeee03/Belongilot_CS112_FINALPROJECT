import csv
import os
import time

def Balance(balance):
    print('║ Your balance is currently: ₱', balance)

def Deposit(balance):
    deposit = eval(input('║ Please Enter Amount: '))
    if deposit < 100:
        print('║ Amount insufficient, please enter an amount greater than 100')
        return balance
    else:
        current = balance + deposit
        print('║ Your balance is now: ₱', current)
        return current

def Withdraw(balance):
    withdraw = eval(input('║ Please Enter amount: '))
    if withdraw < 100:
        print('║ Amount insufficient, please enter an amount greater than 100')
        return balance
    elif balance < withdraw:
        print('║ You have insufficient balance!')
        return balance
    else:
        current = balance - withdraw
        print("║ You have withdrawn ₱", withdraw, ", your current balance is ₱", current)
        return current

def database():
    if not os.path.exists("C&Mserver.csv"):
        with open("C&Mserver.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["pin", "balance"])

def load(pin):
    with open("C&Mserver.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["pin"] == str(pin):
                return int(row["pin"]), int(row["balance"])
    return None, None

def save(pin, balance):
    data = []
    with open("C&Mserver.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["pin"] == str(pin):
                row["balance"] = str(balance)
            data.append(row)

    with open("C&Mserver.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["pin", "balance"])
        writer.writeheader()
        writer.writerows(data)

def register():
    pin = int(input("║ Set PIN: "))
    confirm = int(input("║ Confirm PIN: "))

    if pin != confirm:
        print("║ PIN does not match! Please try again\n")
        return register()

    with open("C&Mserver.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pin, 0])

    print("║ Registration successful! You may start your transaction\n")
    return pin, 0

def show_loading():
    print("║ Loading", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

database()

while True:
    print("║━━━━━━━━━━━━━━━Welcome to C&M Banking━━━━━━━━━━━━━━━║")
    print("║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║")
    
    choice = input("║ Are you a registered user? (yes/no): ")
    
    if choice.lower() in ["yes", "y"]:
        entered_pin = int(input("|Enter PIN: "))
        pin, balance = load(entered_pin)

        if pin is None:
            print("║ User not found! Please register.")
            show_loading()
            continue
        
        print("║ Login successful!\n")
    else:
        pin, balance = register()

    while True:
        print("║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║")
        print("║ Would you like to: \n║ (D)eposit \n║ (W)ithdraw \n║ (B)alance Check \n║ (X) Logout")
        print("║ Current Balance: ₱", balance)
        choice = input("║ Enter desired transaction here ('D'/'W'/'B'/'X'): ")

        show_loading()

        if choice.lower() == 'b':
            Balance(balance)

        elif choice.lower() == 'd':
            balance = Deposit(balance)

        elif choice.lower() == 'w':
            balance = Withdraw(balance)

        elif choice.lower() == 'x':
            save(pin, balance)
            print('║ Thank you for using C&M Banking! \n')
            show_loading()
            break

        else:
            print("║ Invalid Operation!\n")

        show_loading()

        another = input('║ Do you want to make another transaction (yes/no)? ')
        if another.lower() != 'yes':
            save(pin, balance)
            print('║ Thank you for using C&M Banking! \n')
            show_loading()
            break
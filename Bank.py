import random
accounts = {}
def create_account():
    name = input("Enter Account Holder Name: ")
    initial_deposit = float(input("Enter Initial Deposit Amount: "))
    acc_num = str(random.randint(10000, 99999))
    while acc_num in accounts:
        acc_num = str(random.randint(10000, 99999))
    accounts[acc_num] = {
        'name': name,
        'balance': initial_deposit,
        'history': [f"Account created. Balance: {initial_deposit}"],
        'blocked': False
    }
    print(f"\nAccount Created Successfully!")
    print(f"Your Account Number is: {acc_num}")
def check_security(acc_num):
    if acc_num not in accounts:
        print("\nAccount not found!")
        return False
    if accounts[acc_num]['blocked']:
        print("\nAccount is BLOCKED due to security reasons!")
        return False
    attempts = 0
    while attempts < 3:
        name_check = input("Enter Account Holder Name to verify: ")
        if name_check == accounts[acc_num]['name']:
            return True
        else:
            attempts += 1
            remaining = 3 - attempts
            print(f"Incorrect Name! {remaining} attempts left.")
    accounts[acc_num]['blocked'] = True
    print("\nToo many failed attempts! Account has been BLOCKED.")
    return False
def deposit():
    acc_num = input("Enter Account Number: ")
    if acc_num in accounts:
        if accounts[acc_num]['blocked']:
            print("\nAccount is BLOCKED! Cannot deposit.")
            return
        amount = float(input("Enter Amount to Deposit: "))
        if amount > 0:
            accounts[acc_num]['balance'] += amount
            accounts[acc_num]['history'].append(f"Deposited: +{amount}")
            print(f"\nDeposit Successful! New Balance: {accounts[acc_num]['balance']}")
        else:
            print("\nInvalid amount.")
    else:
        print("\nAccount not found!")
def withdraw():
    acc_num = input("Enter Account Number: ")
    if check_security(acc_num):
        amount = float(input("Enter Amount to Withdraw: "))
        current_balance = accounts[acc_num]['balance']
        if 0 < amount <= current_balance:
            accounts[acc_num]['balance'] -= amount
            accounts[acc_num]['history'].append(f"Withdrawn: -{amount}")
            print(f"\nWithdrawal Successful! Remaining Balance: {accounts[acc_num]['balance']}")
        elif amount > current_balance:
            print("\nInsufficient Funds!")
        else:
            print("\nInvalid amount.")
def check_balance():
    acc_num = input("Enter Account Number: ")
    if check_security(acc_num):
        user = accounts[acc_num]
        print("\n--- Account Details ---")
        print(f"Account Number : {acc_num}")
        print(f"Holder Name    : {user['name']}")
        print(f"Current Balance: {user['balance']}")
        print("-----------------------")
def transaction_history():
    acc_num = input("Enter Account Number: ")
    if check_security(acc_num):
        print(f"\n--- History for {acc_num} ---")
        for record in accounts[acc_num]['history']:
            print(record)
        print("---------------------------")
def main_menu():
    while True:
        print("\n=== BANKING MANAGEMENT SYSTEM ===")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            transaction_history()
        elif choice == '6':
            print("Exiting system.")
            break
        else:
            print("Invalid choice! Please try again.")
main_menu()
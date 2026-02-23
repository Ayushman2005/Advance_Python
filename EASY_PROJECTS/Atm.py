CP = "1234"
MA = 3
attempts = 0
while attempts <= MA:
    entered_pin = input("Enter 4-digit ATM PIN: ")
    if len(entered_pin) != 4:
        print("Invalid PIN format. Enter exactly 4 digits.")
        attempts += 1
        print(f"Attempts left: {MA - attempts}")
        continue
    if entered_pin == CP:
        print("Access granted.")
        break
    else:
        attempts += 1
        print(f"Wrong PIN. Attempts left: {MA - attempts}")
if attempts > MA:
    print("Your card has been blocked. Please contact the bank.")
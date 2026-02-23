def Password_Checker():
    password = input("Enter a password:")
    
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    
    if password.isalpha():
        print("Password must contain at least one number.")
        return False
    
    if password.isdigit():
        print("Password must contain at least one letter.")
        return False
    
    for c in password:
        if c in "!@#$%^&*()":
            print("Password must not contain special characters.")
            return False
    
    print("Password is valid.")
    
Password_Checker()
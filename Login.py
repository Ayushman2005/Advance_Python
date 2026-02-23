saved_user = "admin"
saved_pass = "1234"
for i in range(3):
    user = input("Username: ")
    pwd = input("Password: ")
    if user == saved_user and pwd == saved_pass:
        print("Login Successful")
        break
    else:
        print("Wrong credentials")
else:
    print("Account locked")
pass1 = input("Enter the Password:")
while True:
  if pass1 == 'admin':
    print("Accessible")
    break
  else:
    print("Not Accessible")
    pass1 = input("Enter the Password:")
    continue
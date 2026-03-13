from tkinter import *

def submit():
    print("Name:", name_entry.get())
    print("Email:", email_entry.get())
    print("Password:", password_entry.get())
    print("Phone:", phone_entry.get())
    print("Age:", age_entry.get())
    print("Gender:", gender_entry.get())

root = Tk()
root.title("Registration Form")
root.geometry("500x600")

name = Label(root, text="Name")
name.pack()
name_entry = Entry(root)
name_entry.pack()

email = Label(root, text="Email")
email.pack()
email_entry = Entry(root)
email_entry.pack()

password = Label(root, text="Password")
password.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

phone = Label(root, text="Phone")
phone.pack()
phone_entry = Entry(root)
phone_entry.pack()

age = Label(root, text="Age")
age.pack()
age_entry = Entry(root)
age_entry.pack()

gender = Label(root, text="Gender")
gender.pack()
gender_entry = Entry(root)
gender_entry.pack()

Button(root, text="Submit", command=submit).pack()

root.mainloop()
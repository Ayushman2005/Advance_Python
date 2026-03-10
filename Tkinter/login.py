import tkinter as tk

root = tk.Tk()
root.title("Facebook Login")
root.geometry("400x500")
root.configure(bg="white")

title = tk.Label(root, text="Log in to Facebook",bg="white",fg="black")
title.pack(pady=(10,20))

email_label = tk.Label(root, text="Email or phone number",bg="white",fg="black")
email_label.pack(pady=(0,5))

email = tk.Entry(root)
email.pack(pady=10, ipady=8)


password_label = tk.Label(root, text="Password",bg="white",fg="black")
password_label.pack(pady=(0,5))

password = tk.Entry(root, show="*")
password.pack(pady=10, ipady=8)


login_btn = tk.Button(root,text="Log in",bg="blue",fg="white",width=25,pady=8)
login_btn.pack(pady=15)


forgot = tk.Label(root,text="Forgotten password?",fg="blue",bg="white")
forgot.pack(pady=5)


create_btn = tk.Button(root,text="Create new account",bg="white",fg="blue",width=25,pady=8,highlightbackground="blue")
create_btn.pack(pady=10)


meta = tk.Label(root,text="Meta",bg="white",fg="black")
meta.pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

def register():
    roll_no = entry_rollno.get()
    reg_no = entry_regno.get()
    username = entry_username.get()
    password = entry_password.get()
    
    if roll_no and reg_no and username and password:
        messagebox.showinfo("Success", f"Registration successful for {username}!")
    else:
        messagebox.showerror("Error", "Please fill all fields")

root = tk.Tk()
root.title("GIET University")
root.geometry("400x500")

bg_color = "#e8f4f8"
primary_color = "#0056b3"
accent_color = "#ff9900"
entry_bg = "#ffffff"

root.configure(bg=bg_color)

header_frame = tk.Frame(root, bg=primary_color, pady=20)
header_frame.pack(fill=tk.X)

tk.Label(header_frame, text="GIET University", font=("Arial", 20, "bold"), fg="white", bg=primary_color).pack()
tk.Label(header_frame, text="Student Registration Portal", font=("Arial", 12, "italic"), fg=accent_color, bg=primary_color).pack()

form_frame = tk.Frame(root, bg=bg_color, pady=30, padx=40)
form_frame.pack(fill=tk.BOTH, expand=True)

label_font = ("Arial", 11, "bold")
entry_font = ("Arial", 11)

tk.Label(form_frame, text="Roll No.", font=label_font, bg=bg_color, fg=primary_color).pack(anchor="w")
entry_rollno = tk.Entry(form_frame, font=entry_font, bg=entry_bg, relief=tk.FLAT, highlightthickness=1, highlightbackground=primary_color, highlightcolor=accent_color)
entry_rollno.pack(fill=tk.X, pady=(0, 15), ipady=5)

tk.Label(form_frame, text="Registration No.", font=label_font, bg=bg_color, fg=primary_color).pack(anchor="w")
entry_regno = tk.Entry(form_frame, font=entry_font, bg=entry_bg, relief=tk.FLAT, highlightthickness=1, highlightbackground=primary_color, highlightcolor=accent_color)
entry_regno.pack(fill=tk.X, pady=(0, 15), ipady=5)

tk.Label(form_frame, text="Username", font=label_font, bg=bg_color, fg=primary_color).pack(anchor="w")
entry_username = tk.Entry(form_frame, font=entry_font, bg=entry_bg, relief=tk.FLAT, highlightthickness=1, highlightbackground=primary_color, highlightcolor=accent_color)
entry_username.pack(fill=tk.X, pady=(0, 15), ipady=5)

tk.Label(form_frame, text="Password", font=label_font, bg=bg_color, fg=primary_color).pack(anchor="w")
entry_password = tk.Entry(form_frame, font=entry_font, show="*", bg=entry_bg, relief=tk.FLAT, highlightthickness=1, highlightbackground=primary_color, highlightcolor=accent_color)
entry_password.pack(fill=tk.X, pady=(0, 25), ipady=5)

btn_submit = tk.Button(form_frame, text="Register Now", font=("Arial", 12, "bold"), bg=primary_color, fg="white", activebackground=accent_color, activeforeground="white", relief=tk.FLAT, cursor="hand2", command=register)
btn_submit.pack(fill=tk.X, ipady=8)

tk.Label(root, text="© 2026 GIET University", font=("Arial", 9), bg=bg_color, fg="#888888").pack(pady=10)

root.mainloop()

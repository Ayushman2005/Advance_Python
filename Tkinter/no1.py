from tkinter import *

root = Tk()
root.title("My First GUI App")
root.geometry("400x300")

label = Label(root, text="Welcome to Python GUI Programming")
label.pack(pady=100)

root.mainloop()
from tkinter import *

def say_hello():
    print("Hello Students! Welcome to Tkinter")

root = Tk()
root.title("Button Example")
root.geometry("300x200")

button = Button(root, text="Click Me", command=say_hello)
button.pack(pady=80)

root.mainloop()
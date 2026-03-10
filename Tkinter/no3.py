from tkinter import *

def greet():
    name = entry.get()
    print(f"Hello {name}")

root = Tk()
root.title("User Input")
root.geometry("300x200")

label = Label(root, text="Enter your name:")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Submit", command=greet)
button.pack(pady=10)

root.mainloop()
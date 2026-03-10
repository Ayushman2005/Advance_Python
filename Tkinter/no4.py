from tkinter import *

def submit_feedback():
    feedback = text_box.get()
    print("Feedback:", feedback)

root = Tk()
root.title("Feedback App")
root.geometry("400x300")

label = Label(root, text="Write your feedback:")
label.pack()

text_box = Text(root, height=10, width=40)
text_box.pack()

button = Button(root, text="Submit Feedback", command=submit_feedback)
button.pack(pady=10)

root.mainloop()
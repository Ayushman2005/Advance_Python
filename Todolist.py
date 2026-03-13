from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List")
root.geometry("400x500")

tasks = {}

def refresh_list():
    task_box.delete(0, END)
    for num, task in tasks.items():
        task_box.insert(END, f"{num}. {task}")

def add_task():
    task = task_entry.get()
    if task:
        num = len(tasks) + 1
        tasks[num] = task
        refresh_list()
        task_entry.delete(0, END)

def delete_task():
    try:
        num = int(delete_entry.get())

        if num not in tasks:
            messagebox.showerror("Error", "Task number not present")
            return

        del tasks[num]

        new_tasks = {}
        i = 1
        for task in tasks.values():
            new_tasks[i] = task
            i += 1

        tasks.clear()
        tasks.update(new_tasks)

        refresh_list()
        delete_entry.delete(0, END)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

task_box = Listbox(root)
task_box.pack()

Label(root, text="Enter task").pack()
task_entry = Entry(root)
task_entry.pack()

Button(root, text="Add Task", command=add_task).pack()

Label(root, text="Task number to delete").pack()
delete_entry = Entry(root)
delete_entry.pack()

Button(root, text="Delete Task", command=delete_task).pack()

root.mainloop()
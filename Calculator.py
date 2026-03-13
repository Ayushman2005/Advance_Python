from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("320x420")
root.config(bg="black")

temp = ""
flag = False

display = Label(root, text="0", anchor="e", width=14, font=("Arial",28), bg="black", fg="white")
display.grid(row=0, column=0, columnspan=4, pady=10)


def click(num):
    global temp, flag

    num = str(num)

    if flag and num not in "+-*/":
        temp = num
        flag = False

    elif flag and num in "+-*/":
        flag = False
        temp += num

    else:
        if temp == "" and num in "*/":
            return

        if temp and temp[-1] in "+-*/" and num in "+-*/":
            temp = temp[:-1] + num
        else:
            temp += num

    display.config(text=temp)


def res():
    global temp, flag
    temp = str(eval(temp))
    display.config(text=temp)
    flag = True


def clear():
    global temp, flag
    temp = ""
    display.config(text="0")
    flag = False


num_color = "#f39c12"
op_color = "#1abc9c"

Button(root,text="7",width=5,height=2,font=("Arial",16),bg=num_color,fg="white",command=lambda:click(7)).grid(row=1,column=0)
Button(root,text="8",width=5,height=2,font=("Arial",16),bg=num_color,fg="white",command=lambda:click(8)).grid(row=1,column=1)
Button(root,text="9",width=5,height=2,font=("Arial",16),bg=num_color,fg="white",command=lambda:click(9)).grid(row=1,column=2)

Button(root,text="4",width=5,height=2,font=("Arial",16),bg=num_color,fg="white",command=lambda:click(4)).grid(row=2,column=0)
Button(root,text="5",width=5,height=2,font=("Arial",16),bg=num_color,fg="white",command=lambda:click(5)).grid(row=2,column=1)
Button(root,text="6",width=5,height=2,font=("Arial",16),bg=num_color,fg="white",command=lambda:click(6)).grid(row=2,column=2)

Button(root,text="1",width=5,height=2,font=("Arial",16),bg=num_color,fg="white",command=lambda:click(1)).grid(row=3,column=0)
Button(root,text="2",width=5,height=2,font=("Arial",16),bg=num_color,fg="white",command=lambda:click(2)).grid(row=3,column=1)
Button(root,text="3",width=5,height=2,font=("Arial",16),bg=num_color,fg="white",command=lambda:click(3)).grid(row=3,column=2)

Button(root,text="0",width=5,height=2,font=("Arial",16),bg=num_color,fg="white",command=lambda:click(0)).grid(row=4,column=1)

Button(root,text="+",width=5,height=2,font=("Arial",16),bg=op_color,fg="white",command=lambda:click("+")).grid(row=1,column=3)
Button(root,text="-",width=5,height=2,font=("Arial",16),bg=op_color,fg="white",command=lambda:click("-")).grid(row=2,column=3)
Button(root,text="*",width=5,height=2,font=("Arial",16),bg=op_color,fg="white",command=lambda:click("*")).grid(row=3,column=3)
Button(root,text="/",width=5,height=2,font=("Arial",16),bg=op_color,fg="white",command=lambda:click("/")).grid(row=4,column=3)

Button(root,text="C",width=5,height=2,font=("Arial",16),bg="#16a085",fg="white",command=clear).grid(row=4,column=0)
Button(root,text="=",width=5,height=2,font=("Arial",16),bg="#2ecc71",fg="white",command=res).grid(row=4,column=2)

root.mainloop()
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()

def data():
    id=userid.get()
    password=pass_entery.get()
    print(f"User ID: {id}\nPassword: {password}")


    if id=="giet" and password=="1234":
        messagebox.showinfo("Login", "Login successful") 
        print("Login successful")
    else:
        messagebox.showerror("Login", "Login failed")   
        print("Login failed")   

root.title("SASTA LOGIN PAGE")
root.minsize(100, 100)
root.maxsize(900, 900)
root.geometry("300x700")
root.config(bg="yellow")

# image label
img=Image.open("pic.png")
resize_img=img.resize((80, 90))
img=ImageTk.PhotoImage(resize_img)
img_label=Label(root,image=img)
img_label.pack(pady=(18,2))
img_label.config(bg="black")

#text label
text_label=Label(root,text="INSTAGRAM",font=("courier", 26))
text_label.pack(pady=(8,18))
text_label.config(bg="yellow",fg="black")

#credentials label

userid_label=Label(root,text="Enter User ID",font=("courier", 16))
userid_label.pack(pady=(8,18))
userid_label.config(bg="yellow",fg="black")

userid=Entry(root,width=30)
userid.pack(ipady=8,pady=(0,18))


pass_label=Label(root,text="Enter Password",font=("courier", 16))
pass_label.pack(pady=(8,18))
pass_label.config(bg="yellow",fg="black")

pass_entery=Entry(root,width=30,show="*")
pass_entery.pack(ipady=8,pady=(0,18))

#button label

Btn=Button(root,text="Login",font=("italic", 16),command=data)
Btn.config(bg="white",fg="black",activebackground="blue",activeforeground="white",width=6,height=3)
Btn.pack(pady=(18,8))


exit=Button(root,text="EXIT",font=("italic", 16),command=root.destroy)
exit.config(bg="black",fg="white",activebackground="blue",activeforeground="white",width=6,height=3)
exit.pack(pady=(18,8))

check=Checkbutton(root,text="Remember me",bg="yellow",fg="black")
check.pack(pady=(18,8))

#pip install Pillow

root.mainloop()
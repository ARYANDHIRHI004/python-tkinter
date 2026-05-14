from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("500x600")

username = StringVar()
password = StringVar()

def handelSubmit():
    if(len(username.get())==0 or len(password.get())==0):
        tmsg.showwarning("warning", "Finds are empty..!")
        return 
    with open("db.txt", 'a') as f:
        f.write(f"Username is {username.get()}, password is {password.get()}\n")
        username.set(""), password.set("")
        tmsg.showinfo("Thanks", "user stored in db..")

l1 = Label(root, text="This is login form")
l1.grid(row=0, column=3)
user = Label(root, text="Username")
passwd = Label(root, text="Password")

user.grid(row=1)
passwd.grid(row=2)

userEntry = Entry(root, textvariable=username)
passEntry = Entry(root, textvariable=password)
userEntry.grid(row=1, column=1)
passEntry.grid(row=2, column=1)

submit = Button(root, text="Submit", command=handelSubmit)
submit.grid(row=3, column=2)

root.mainloop()
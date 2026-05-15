from tkinter import *

root =  Tk()
root.geometry("344x500")
root.title("Calculator by Aryan Dhirhi")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, padx=10, pady=10) 

numbers = [1,2,3,4,5,6,7,8,9,0, "c", "=", "+", "-"]

f1 = Frame(root, bg="grey")
f1.pack()

def click(event):
    text = event.widget.cget("text")
    if(text == "="):
        scvalue.set(eval(scvalue.get()))
    if(text == "c"):
        scvalue.set("")
    else:
        if(text != "="):
            scvalue.set(scvalue.get() + text)
            screen.update()
        
    

for number in numbers:
    b = Button(f1, text=f"{number}", name=f"{number}", font="lucida 35 bold")
    b.pack( side=LEFT, padx=10,ipadx=10, pady=10)
    b.bind("<Button-1>", click)


root.mainloop()


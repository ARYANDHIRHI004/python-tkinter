from tkinter import *

root = Tk()

root.geometry("500x800")

f1 = Frame(root, bg="grey")
f1.pack(side=LEFT, fill=Y)

def click():
    print("I am Clicked")

b1 = Button(f1, text="Chick Me 1", command=click)
b1.pack()

b2 = Button(f1, text="Chick Me 2")
b2.pack()

b3 = Button(f1, text="Chick Me 3")
b3.pack()

b4 = Button(f1, text="Chick Me 4")
b4.pack()
root.mainloop()
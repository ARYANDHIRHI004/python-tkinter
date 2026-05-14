from tkinter import *

root = Tk()

root.title("Tute 3")
root.geometry("500x800")

f1 = Frame(root, bg="grey", width=500)

f2 = Frame(root, bg="grey")
f2.pack(fill=X, )
f1.pack(fill=Y, side=LEFT )


l1 = Label(f1, text="This is frame one.", relief="raised")
l1.pack(padx=5, pady=10)

l2 = Label(f2, text="This is Nav Bar")
l2.pack( pady=10 )


root.mainloop()
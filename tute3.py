from tkinter import *

root = Tk()

root.title("Tute 3")
root.geometry("500x800")

f1 = Frame(root, bg="grey")
f1.pack(fill=Y, side=LEFT )
l1 = Label(f1, text="This is frame one.")
l1.pack( fill=Y)


root.mainloop()
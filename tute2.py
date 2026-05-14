from tkinter import *

root = Tk()
root.minsize(400,300)

root.title("This is our first software")

l1 = Label(root, text="Hello Everyone this is tkinter's series", bg="Red", fg="white", padx=5)
l1.pack()

root.mainloop()
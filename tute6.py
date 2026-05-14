from tkinter import *

root = Tk()

m1 = Menu(root)
root.config(menu=m1)

file = Menu(m1, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_separator()
file.add_command(label="Save")
file.add_command(label="Save As")

edit = Menu(m1, tearoff=0)
edit.add_command(label="Quit", command=quit)



m1.add_cascade(label="File", menu=file)
m1.add_cascade(label="Edit", menu=edit)


root.mainloop()

from tkinter import *

root = Tk()

def show():
    if var.get() == 0:
        myLabel = Label(root, text = "No").pack()
    else: 
        myLabel = Label(root, text = "Yes").pack()
    

var = IntVar()

c = Checkbutton(root, text = "Check this Box. It is a dare.", variable=var)
c.pack()

mybutton = Button(root, text = "Show Me.", command=show).pack()

root.mainloop()
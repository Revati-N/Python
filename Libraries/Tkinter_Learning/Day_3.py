from tkinter import *

root = Tk()

e = Entry(root, width = 50, bg= "#ffbf00", fg = "#471143")
e.pack()
e.insert(0, "Name")

def myClick():
    myLabel = Label(root, text = "Hello " + e.get()+ " ...")
    myLabel.pack()

myButton = Button(root, text = "Click Me", command=myClick)
myButton.pack()

root.mainloop()
from tkinter import *

root = Tk()

def click1():
    mylabel = Label(root, text ="You clicked colour the button.")
    mylabel.pack()


def click2():
    mylabel = Label(root, text ="You clicked the big button.")
    mylabel.pack()

def click4():
    mylabel = Label(root, text ="You clicked the colorful button.")
    mylabel.pack()

mybutton1 = Button(root, text = "Click Me", command=click1) # Just a button which returns a message
mybutton2 = Button(root, text = "Click Me", state=DISABLED)     # Disabled button
mybutton3 = Button(root, text = "Click Me", padx=50, pady=20, command=click2)  # Dimensions to button returning message
mybutton4 = Button(root, text = "Click Me", fg="#471143", bg="yellow", command=click4) # bg is for background color and fg is for font color

mybutton1.pack()
mybutton2.pack()
mybutton3.pack()
mybutton4.pack()

root.mainloop()
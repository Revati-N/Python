from tkinter import *
from tkinter import messagebox

def new():
    Top = Toplevel()
    lbl = Label(Top, text = 'Bye Bye').pack()
    button2 = Button(Top, text = 'Close', command=Top.destroy).pack()

root = Tk()
label = Label(root, text ="Hello World!").pack()
button = Button(root, text = 'Click', command=new).pack()


root.mainloop()
from tkinter import *

root = Tk()

#root.geometry("500x500")

def show():
    mylabel = Label(root, text = clicked.get()).pack()

clicked = StringVar()
clicked.set("RM")

drop = OptionMenu(root, clicked, "RM","Jin","Suga","JHope","Jimin","V","JK")
drop.pack()

mybutton = Button(root, text="Show", command=show).pack()

root.mainloop()
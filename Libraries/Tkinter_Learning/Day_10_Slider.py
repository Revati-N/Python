from tkinter import *
from PIL import ImageTk,Image


root = Tk()

Hi = Label(root, text="Hello!\n Here are 2 sliders.")
Hi.pack()

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()


root.mainloop()
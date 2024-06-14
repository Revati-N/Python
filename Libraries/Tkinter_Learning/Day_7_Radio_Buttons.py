from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Day 7')

Bands = [
    ("BTS","BTS"),
    ("Beatles","Beatles"),
    ("One Direction","One Direction"),
    ("Jonas Brothers","Jonas Brothers")
]

BoyBands = StringVar()
BoyBands.set("BTS")

for text, boys in Bands:
    Radiobutton(root,text=text, variable=BoyBands, value = boys).pack(anchor = W)

def clicked(value):
	myLabel = Label(root, text=value)
	myLabel.pack()	

mainloop()
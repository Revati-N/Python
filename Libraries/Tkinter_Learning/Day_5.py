from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("My GUI")

button_quit = Button(root, text = "Exit", command = root.quit)
button_quit.pack()

root.mainloop()
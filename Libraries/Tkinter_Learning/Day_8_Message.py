from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Messages')

def popup():
	response = messagebox.showinfo("This is my Popup!", "Hello World!") #opens a new window showing 'hello world' with an info symbol
	warn = messagebox.showwarning("This is my Popup!", "Hello World!")  #opens a new window showing 'hello world' with a warning symbol
	errors = messagebox.showerror("This is my Popup!", "Hello World!")  #opens a new window showing 'hello world' with an error symbol
	ask = messagebox.askquestion("This is my Popup!", "Click Yes or No")  #opens a new window showing 'hello world' with a question
	if ask == "yes":
		Label(root, text="You clicked Yes!").pack()
	else: 
		Label(root, text="You clicked No!!").pack()
	# Alongside 'askquestion', we can also use 'askokcancel' and 'askyesno'
Label(root).pack() 

Button(root, text = "Pop It", command = popup).pack()

root.mainloop()
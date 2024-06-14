from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root. title("Plots")

def graph():
    grocery_prices = np.random.normal(100000, 1000,100)
    plt.hist(grocery_prices, 50)
    plt.show()

mybutton = Button(root, text="Graph it.", command=graph).pack()

root.mainloop()

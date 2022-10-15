from logging import root
import tkinter as tk
from tkinter import *

root =Tk()
root.geometry("500x500")
listSample = Listbox(root,width=70,height=30,
fg="blue",font=("Arial 28"))
listSample.insert(1,"pizza1")
listSample.insert(2,"pizza2")
listSample.insert(3,"pizza3")

listSample.pack()
root,mainloop()

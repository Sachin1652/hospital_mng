import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background = "black")



        title = Label(self.root,text="Member Registration form", font=("monotype corsive",30,"bold"),bd=5,relief=GROOVE,bg="#E6005C",fg="#000000")
        title.pack(side=TOP,fill=X)

        manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#001a66")
        manage_Frame.place(x=20,y=100,width=450,height=630)


if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
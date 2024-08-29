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


        Date_of_registration = StringVar()
        Date_of_registration.set(time.strftime("%d/%m/%y"))        


        title = Label(self.root,text="Member Registration form", font=("monotype corsive",30,"bold"),bd=5,relief=GROOVE,bg="#E6005C",fg="#000000")
        title.pack(side=TOP,fill=X)

        manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#001a66")
        manage_Frame.place(x=20,y=100,width=450,height=630)


        detail_frame = Frame(self.root,relief=RIDGE,bg="#001a66")
        detail_frame.place(x=500,y=100,width=820,height=630)


        Cus_title = Label(manage_Frame,text="Customer Details",font=("arial",20,"bold"),bg="#001a66",fg="white")
        Cus_title.grid(row=0,columnspan=2,pady=5)

        member_datelbl = Label(manage_Frame,text="Data",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_datelbl.grid(row=1,column=0,pady=10,sticky="w")

        member_datetxt = Entry(manage_Frame,font=("arial",15,"bold"),textvariable=Date_of_registration)
        member_datetxt.grid(row=1,column=1,pady=5,padx=10,sticky="w")


if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
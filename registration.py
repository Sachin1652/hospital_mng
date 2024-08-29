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

        Ref = StringVar()
        Mobile_no = StringVar()
        Pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()  


        Membership = StringVar()
        Membership.set("0")


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

        member_reflb1 = Label(manage_Frame,text="Reference ID",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_reflb1.grid(row=2,column=0,pady=5,padx=10,sticky="w")

        member_reftxt = Entry(manage_Frame,font=("arial",15,"bold"),state=DISABLED,Text=Ref)
        member_reftxt.grid(row=2,column=1,pady=5,padx=10,sticky="w")

        member_fnamelbl = Label(manage_Frame,text="First Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_fnamelbl.grid(row=3,column=0,pady=10,sticky="w")

        member_fnametxt = Entry(manage_Frame,font=("arial",15,"bold"),textvariable=Firstname)
        member_fnametxt.grid(row=3,column=1,pady=5,padx=10,sticky="w")

        member_lnamelbl = Label(manage_Frame,text="Last Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_lnamelbl.grid(row=4,column=0,pady=10,sticky="w")

        member_lnametxt = Entry(manage_Frame,font=("arial",15,"bold"),textvariable=Lastname)
        member_lnametxt.grid(row=4,column=1,pady=5,padx=10,sticky="w")

        member_mobilelbl = Label(manage_Frame,text="Mobile No",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_mobilelbl.grid(row=5,column=0,pady=10,sticky="w")

        member_mobiletxt = Entry(manage_Frame,font=("arial",15,"bold"),textvariable=Mobile_no)
        member_mobiletxt.grid(row=5,column=1,pady=5,padx=10,sticky="w")

        member_addresslbl = Label(manage_Frame,text="Address",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_addresslbl.grid(row=6,column=0,pady=10,sticky="w")

        member_addresstxt = Entry(manage_Frame,font=("arial",15,"bold"),textvariable=Address)
        member_addresstxt.grid(row=6,column=1,pady=5,padx=10,sticky="w")

        member_pincodelbl = Label(manage_Frame,text="Pin Code",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_pincodelbl.grid(row=7,column=0,pady=10,sticky="w")

        member_pincodetxt = Entry(manage_Frame,font=("arial",15,"bold"),textvariable=Pincode)
        member_pincodetxt.grid(row=7,column=1,pady=5,padx=10,sticky="w")

        member_genderlbl = Label(manage_Frame,text="Gender",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_genderlbl.grid(row=8,column=0,pady=10,sticky="w")

        member_gendercmb = ttk.Combobox(manage_Frame,Text=var4,state="readonly",font=("arial",15,"bold"),width=19)
        member_gendercmb['values']=("","Male","Female","Other")
        member_gendercmb.current(0) #when nothing it will set auto empty 
        member_gendercmb.grid(row=8,column=1,pady=5,padx=10,sticky="w")


if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
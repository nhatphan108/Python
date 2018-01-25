from tkinter import *
from admin import is_admin
from admin import run_as_admin
import tkinter.messagebox
import socket
import re
import os


is_View = False
window = Tk()

def excecute_the_program():
    run_as_admin("admin.py")


'''os.startfile("WebsiteBlocker.pyw")
window.destroy()'''

def return_weblist():
    with open("websites.txt","r") as w:
        listofwebs = w.readlines()
        w.close()
    return listofwebs
#Check if website is valid or not
def is_website_valid(website):
    try:
        socket.gethostbyname(website)
    except socket.gaierror:
        return False
    else:
        return True

def UpdateTime():
    timeframe = [ i for i in range(0,24)]
    try:
        begintime = int(from_text.get())
        stoptime= int(to_text.get())
    except ValueError:
        tkinter.messagebox.showinfo("Warning","Invalid input. Input has to be integers")
    else:
        if all(i in timeframe for i in [begintime,stoptime]):
            if (stoptime > begintime) and (begintime > 0):
                with open("time.txt","w+") as t:
                    t.write(str(begintime) + "\n")
                    t.write(str(stoptime) + "\n")
                    t.close()
            else:
                tkinter.messagebox.showinfo("Warning","Time from which the program starts must be before the time the program ends and beginning time needs to be larger than 0")
        else:
            tkinter.messagebox.showinfo("Warning","Timeframe has to be from 0 to 23")

def ViewAll():
    global is_View
    listofwebs = return_weblist()
    if (is_View == False):
        list1.delete(0,END)
        for i in listofwebs:
            list1.insert(END,i.rstrip("\n"))
            is_View = True
    else:
        list1.delete(0,END)
        is_View = False

def AddWebsite():
    if is_website_valid(addwebsite_text.get()):
        with open("websites.txt","a+") as w:
            w.seek(0)
            listofwebs = w.readlines()
            listofwebs2 = [i.rstrip("\n") for i in listofwebs]
            w.seek(0)
            if not (addwebsite_text.get()) in listofwebs2:
                w.write(addwebsite_text.get() + "\n")
                is_View = False
                ViewAll()
                w.close()
            else:
                tkinter.messagebox.showinfo("Warning","Website already on the list")
                w.close()
    else:
        tkinter.messagebox.showinfo("Warning","Website is not valid online")



def get_selected_row(event):
    try:
        global selected
        index = (list1.curselection())
        selected = list1.get(index)
    except tkinter.TclError:
        pass

def delete_website():
    global is_View
    listofwebs = return_weblist()
    listofwebs = [i.rstrip("\n") for i in listofwebs]
    try:
        listofwebs.remove(selected.rstrip("\n"))
    except NameError:
        tkinter.messagebox.showinfo("Warning","An element must be chosen before actually being deleted")
    with open("websites.txt","w") as w:
        for i in listofwebs:
            w.write(i + "\n")
        w.close()
    is_View = False
    ViewAll()


window.wm_title("Website Blocker")

Helve = ("Helvetica",12,"bold")
BigArial = ("Arial",20,"bold italic")
SmallArial = ("Arial",10,"italic")


l1 = Label(window,text="From",font=Helve,borderwidth=2,relief="sunken")
l1.grid(row=0,column=0)

l2 = Label(window,text="To",font=Helve,borderwidth=2,relief="sunken")
l2.grid(row=0,column=2)
from_text = StringVar()
e1=Entry(window,textvariable = from_text,width=22)
e1.grid(row=0,column=1)

to_text = StringVar()
e2=Entry(window,textvariable = to_text,width=22)
e2.grid(row=0,column=3)

l3=Label(window,text="New Website",font=Helve,borderwidth=2,relief="sunken")
l3.grid(row=1,column=0,columnspan=4)

addwebsite_text = StringVar()
e3=Entry(window,textvariable =addwebsite_text,width=68)
e3.grid(row=2,column=0,columnspan=4)

l4=Label(window,text="Website Blocker",font=BigArial,width=24,borderwidth = 2,relief="solid")
l4.grid(row=3,column=0,columnspan=4)

l5=Label(window,text="This program runs a python script that blocks certain websites in a desginated amount of time",font=SmallArial,width=50,wraplength=210)
l5.grid(row=4,column=0,columnspan=4)

list1 = Listbox(window,height=7,width=40)
list1.grid(row=5,column=0,columnspan=2,rowspan=7)

list1.bind('<<ListboxSelect>>',get_selected_row)
sb1=Scrollbar(window)
sb1.grid(row=5,column=2,rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window,text="View/Close All Websites",width=17,command=ViewAll)
b1.grid(row=5,column=3)

b2 = Button(window,text="Delete Website",width=17,command = delete_website)
b2.grid(row=6,column=3)

b3 = Button(window,text="Update time",width=17,command = UpdateTime)
b3.grid(row=7,column=3)

b4 = Button(window,text="Add Website",width=17,command = AddWebsite)
b4.grid(row=8,column=3)

b5 = Button(window,text="Execute the program",width=17,command= excecute_the_program)
b5.grid(row=9,column=3)
window.mainloop()

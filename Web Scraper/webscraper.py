from tkinter import *
import socket
import tkinter.messagebox
import pandas
import requests
from bs4 import BeautifulSoup


def execute_program():
    website = site_string.get()
    export_valid = True
    propertylist = []
    if (sum([address_checked.get(),price_checked.get(),city_checked.get(),beds_checked.get(),baths_checked.get(),area_checked.get()]) >= 2):
        global soup
        global number
        try:
            r = requests.get(website)
            soup = BeautifulSoup(r.content,"html.parser")
            all = soup.find_all("div",{"class":"property-card-primary-info"})
            number = len(all)
        except:
            tkinter.messagebox.showinfo("Warning","Make sure that you enter the right site !!")
            export_valid = False
        if (export_valid):
            for i in all:
                d = {}
                if price_checked.get() == 1:
                    try:
                        d["Price"]=i.find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ","")
                    except:
                        d["Price"] = "Ungiven"
                if address_checked.get() == 1:
                    try:
                        d["Address"] =i.find("div",{"class":"property-address"}).text.replace("\n","").strip()
                    except:
                        d["Address"] ="Ungiven"
                if city_checked.get() == 1:
                    try:
                        d["City"] = i.find("div",{"class":"property-city"}).text.replace("\n","").strip()
                    except:
                        d["City"] = "Ungiven"

                if beds_checked.get() == 1:
                    try:
                        d["Beds"] = i.find("div",{"class":"property-beds"}).find("strong").text
                    except:
                        d["Beds"] = "Ungiven"

                if baths_checked.get() == 1:
                    try:
                        d["Baths"] = i.find("div",{"class":"property-baths"}).find("strong").text
                    except:
                        d["Baths"] ="Ungiven"

                if area_checked.get() == 1:
                    try:
                        d["Area"] = i.find("div",{"class":"property-sqft"}).find("strong").text
                    except:
                        d["Area"] = "Ungiven"
                propertylist.append(d)
    else:
        tkinter.messagebox.showinfo("Warning","Make sure you have checked at least two boxes!!")
        export_valid = False

    if (export_valid):
        name = soup.find("div",{"class":"results-label"}).find("h1").text.replace(" ","") + ".csv"
        df = pandas.DataFrame(propertylist)
        df.to_csv(name)
        tkinter.messagebox.showinfo("Notification","Success !!! " + str(number) + " results have been pulled from the site and now are in your folder")

window = Tk()
window.wm_title("WebScraper")

Font1 = ("fixedsys",20,"bold")
Font2 = ("fixedsys",12,"italic")
Font3 = ("fixedsys",15,"bold italic")

photo = PhotoImage(file="century21.png")
l1=Label(window,image = photo)
l1.grid(column=0,row=0,columnspan=3)

l2=Label(window,text="Real Estate Web Scraper",font=Font1,relief="sunken")
l2.grid(column=0,row=1,columnspan=3)

l3=Label(window,text="An application that allows you to scrape any data from 21Century Real Estate site with one click.",font = Font2,wraplength=250,width=50)
l3.grid(column=0,row=2,columnspan=3)

l4=Label(window,text="Please choose the data that will be extracted",font=Font2,relief="sunken",width=50)
l4.grid(column=0,row=3,columnspan=3)

price_checked = IntVar()
priceButton = Checkbutton(window,text="Price",font=Font2,variable=price_checked)
priceButton.grid(column=0,row=4,pady=10,padx=30)

address_checked = IntVar()
adddressButton = Checkbutton(window,text="Address",font=Font2,variable =address_checked)
adddressButton.grid(column=1,row=4,pady=10,padx=30)

city_checked = IntVar()
cityButton = Checkbutton(window,text="City",font=Font2,variable=city_checked)
cityButton.grid(column=2,row=4,pady=10)

beds_checked = IntVar()
bedsButton = Checkbutton(window,text="Beds",font=Font2,variable=beds_checked)
bedsButton.grid(column=0,row=5,pady=10,padx=30)

baths_checked = IntVar()
bathsButton = Checkbutton(window,text="Baths",font=Font2,variable=baths_checked)
bathsButton.grid(column=1,row=5,pady=10,padx=30)

area_checked = IntVar()
areaButton = Checkbutton(window,text="Area",font=Font2,variable=area_checked)
areaButton.grid(column=2,row=5,pady=10)

l5 = Label(window,text="Enter the site from which you want to extract data",relief ="sunken",font=Font2,width=50)
l5.grid(column=0,row=6,columnspan=3)

site_string = StringVar()
e1= Entry(window,textvariable=site_string,width=50)
e1.grid(column=0,row=7,columnspan=3)

b1 = Button(window,text="Import the data into a file",font =Font3,command=execute_program)
b1.grid(column=0,row=8,columnspan=3)

window.mainloop()

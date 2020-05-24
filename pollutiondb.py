#!/usr/bin/env python
# coding: utf-8

# In[2236]:


from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import csv
from csv import DictWriter
import os.path
import re
import datetime


# In[2237]:


def validateName(s):
     return bool(re.fullmatch('^[a-zA-z][a-zA-z\s]+',s.strip()))


# In[2238]:


def validVehicleNumber1(s1):
     return bool(re.match('[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{1,2}[0-9]{4}$',s1))


# In[2239]:


def register(): 
    validform=True
    name1=name.get()
        
    phone1=" "
    try:
        phone1=int(Phone.get())
    except ValueError:
        tkinter.messagebox.showerror(title="Error", message="Enter a correct phone number")
        Phone.set("")
        validform=False
        
    vechiletype1=Vechiletype.get()
    Vechilenumber1=Vechilenumber.get().upper()
    Vechiclename1=Vechilename.get()
    DOP1=now.strftime("%d-%m-%Y")
    d1=date1.get()
    m1=month1.get()
    y1=year1.get()
    Validupto1=d1+m1+y1

    if (name1=="" or phone1=="" or vechiletype1=="" or Vechilenumber1=="" or Vechiclename1==""):
        tkinter.messagebox.showerror(title="error", message="please fill all the form")
        name.set("")
        Phone.set("")
        Vechiletype.set("car")
        Vechilenumber.set("")
        Vechilename.set("")
        date1.set("1")
        month1.set("jan")
        year1.set("2020")
        
        
    elif not validateName(name1):
        tkinter.messagebox.showerror(title="Error", message="name should not contain digits or characters")
        name.set("")
        
        
    elif(len(Phone.get())!=10 and Phone.get().isdigit()):
        tkinter.messagebox.showerror(title="Error", message="Phone number is not equal to 10 digits")
        Phone.set("")
    
    elif (validVehicleNumber1(Vechilenumber1)==False):
        tkinter.messagebox.showerror(title="Error", message="please fill correct vechile number")
        Vechilenumber.set("")
        
    else:
        file_exists = os.path.isfile('pollutiondb.csv')
        if validform:
            r1=tkinter.messagebox.askquestion(title="Submit", message="You are about to submit data")
            if r1=="yes":
                with open('pollutiondb.csv', 'a',newline='') as csvfile:
                    fieldname=['name','phn number','vechile type','vechile number','vechile name','dop','valid upto']
                    writer1 = csv.DictWriter(csvfile, fieldnames=fieldname)
                    if not file_exists:
                        writer1.writeheader()

                    writer=csv.writer(csvfile)
                    writer.writerow([name1.strip(),phone1,vechiletype1,Vechilenumber1,Vechiclename1,DOP1,Validupto1])
                csvfile.close()
            else:
                name.set("")
                Phone.set("")
                Vechiletype.set("car")
                Vechilenumber.set("")
                Vechilename.set("")
                date1.set("1")
                month1.set("jan")
                year1.set("2020")
            


# In[ ]:





# In[2240]:


def clear():
    name.set("")
    Phone.set("")
    Vechiletype.set("car")
    Vechilenumber.set("")
    Vechilename.set("")
    date1.set("1")
    month1.set("jan")
    year1.set("2020")
           
    


# In[2241]:


root=Tk()
widthw=990
heightw=330
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x_cord =screen_width/2 -widthw/2
y_cord = screen_height/2 - heightw/2
root.geometry("%dx%d+%d+%d" % (widthw,heightw,x_cord,y_cord))
# root.config(background="dark grey")
root.title("Pollution_form")


# In[ ]:





# In[2242]:


name = StringVar()
Phone = StringVar()
Vechiletype=StringVar()
Vechilenumber=StringVar()
Vechilename=StringVar()
date=StringVar()
month=StringVar()
year=StringVar()
date1=StringVar()
month1=StringVar()
year1=StringVar()
now=StringVar()


# In[2243]:


head=Label(root,text="Pollution DB",font=("arial",24,"bold")).grid(row=0,columnspan=4,padx=20,pady=10)


# In[ ]:





# In[2244]:


lname = Label(root,text = "Name * ").grid(row=1,column=0)
lPhone = Label(root,text = "Phn Number * ",).grid(row=2,column=0)
lvechiletype= Label(root,text = "Vechile Type * ",).grid(row=3,column=0)
lVechilename= Label(root,text = "Vechile Number * ",).grid(row=4,column=0)
lVechiclenumber = Label(root,text = "Vechile Name * ",).grid(row=5,column=0)
lDOP = Label(root,text = "DATE of Pollution* ",).grid(row=6,column=0)
lVupto=Label(root,text = "Valid Upto* ",).grid(row=7,column=0)


# In[2245]:


name_entry = Entry(root,textvariable = name, width = "30").grid(row=1,column=1)
Phone_entry = Entry(root,textvariable = Phone, width = "30").grid(row=2,column=1)
list=["car","scooter","motorcycle"]
droplist=OptionMenu(root,Vechiletype,*list)
droplist.config(width="10",bg = "light blue")
Vechiletype.set("car")
droplist.grid(row=3,column=1)
Vechilenumber_entry = Entry(root,textvariable = Vechilenumber, width = "30").grid(row=4,column=1)
Vechiclename_entry = Entry(root,textvariable = Vechilename, width = "30").grid(row=5,column=1)

now = datetime.datetime.now()
now.strftime("%d-%m-%Y")
lDOPentry = Label(root,text = now.strftime("%d-%m-%Y"),).grid(row=6,column=1)

l5=[]
for i in range(1,32):
    l5.append(i)
droplist=OptionMenu(root,date1,*l5)
droplist.config(width=5,bg = "light blue")
date1.set("1")
droplist.grid(row=7,column=1,padx=0,pady=0)
l6=['Jan','Feb','Mar','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
droplist=OptionMenu(root,month1,*l6)
droplist.config(width=15,bg = "light blue")
month1.set("jan")
droplist.grid(row=7,column=2,padx=0,pady=0)
l7=[]
for x in range(2020,2051):
    l7.append(x)
droplist=OptionMenu(root,year1,*l7)
droplist.config(width=10,bg = "light blue")
year1.set("2020")
droplist.grid(row=7,column=3,padx=0,pady=0)







# In[ ]:





# In[2246]:


register = Button(root,text = "Register",command=register ,width = "30", height = "2", bg = "light grey").grid(row=10,column=0,padx=20,pady=10,sticky=E)
clear = Button(root,text = "Clear",command=clear ,width = "30", height = "2", bg = "light grey").grid(row=10,column=1,padx=20,pady=10,sticky=E)
quit=Button(root,text = "quit",command=root.destroy ,width = "30", height = "2", bg = "light grey").grid(row=10,column=2,padx=20,pady=10,sticky=E)


# In[2247]:


root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





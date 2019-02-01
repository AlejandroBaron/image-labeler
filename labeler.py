# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 12:10:00 2019

@author: bkiller10
"""
from tkinter import *
from PIL import Image, ImageTk
import os
from pathlib import Path



img_dir="unlabeled_jpg"
dest_dir="labeled"
discard_dir="discarded"
images=os.listdir(img_dir)
current=0



my_file = Path("labels.csv")
if my_file.is_file():
    labels_csv  = open("labels.csv", "a")
else:
    labels_csv  = open("labels.csv", "w")
    labels_csv.write("IMG,class,"+os.linesep)


"GUI"
root =  Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
topFrame = Frame(root)
topFrame.grid(row=0,sticky=N+S+E+W)
bottomFrame = Frame(root)
bottomFrame.grid(row=1,sticky=N+S+E+W)

image = Image.open(img_dir+"/"+images[current])
photo = ImageTk.PhotoImage(image)
panel=Label(topFrame,image=photo)
panel.pack()



bottomFrame1=Frame(bottomFrame)
bottomFrame2=Frame(bottomFrame)

bottomFrame1.pack(side=TOP)
bottomFrame2.pack(side=BOTTOM)



"DATA LABELING"
classes=[]
def classify_as(which_class):
    
    global current
    global labels_csv
    
    img_name=images[current][0:-4]
    "Adding img name and classification"
    labels_csv.write(img_name+"_class"+str(which_class)+","+str(which_class)+os.linesep)

    "Moving the picture to the labeled folder"
    os.rename(img_dir+"/"+images[current], dest_dir+"/"+img_name+"_class"+str(which_class)+".jpg")
    "Updating displayed picture"
    next_pic()
    

def discard():
    img_name=images[current][0:-4]
    os.rename(img_dir+"/"+images[current], discard_dir+"/"+images[current])
    next_pic()

def next_pic():
    global current
    current+=1
    image = Image.open(img_dir+"/"+images[current])
    image=image.resize((500,500),Image.ANTIALIAS)
    next_pic = ImageTk.PhotoImage(image)
    panel.config(image = next_pic) 
    panel.photo_ref = next_pic


button0 = Button(bottomFrame1,text="Mammal",bg="green",fg="white",command=lambda : classify_as(0) ,height = 5, width = 20)
button1 = Button(bottomFrame1,text="Bird",bg="green",fg="white",command=lambda : classify_as(1),height = 5, width = 20)
button2 = Button(bottomFrame1,text="Reptile",bg="green",fg="white",command=lambda : classify_as(2),height = 5, width = 20)
button3 = Button(bottomFrame1,text="Fish",bg="green",fg="white",command=lambda : classify_as(3),height = 5, width = 20)
button4 = Button(bottomFrame1,text="Amphibius",bg="green",fg="white",command=lambda : classify_as(4),height = 5, width = 20)
button5 = Button(bottomFrame1,text="Invertebrate",bg="green",fg="white",command=lambda : classify_as(5),height = 5, width = 20)
button6 = Button(bottomFrame2,text="Not an animal",bg="green",fg="white",command=lambda : classify_as(6),height = 5, width = 20)
button7 = Button(bottomFrame2,text="Discard",bg="red",fg="white",command=discard,height = 5, width = 20)

button0.grid(row=0,column=0,sticky=N+S+E+W)
button1.grid(row=0,column=1,sticky=N+S+E+W)
button2.grid(row=0,column=2,sticky=N+S+E+W)
button3.grid(row=1,column=0,sticky=N+S+E+W)
button4.grid(row=1,column=1,sticky=N+S+E+W)
button5.grid(row=1,column=2,sticky=N+S+E+W)
button6.grid(row=0,column=0,sticky=N+S+E+W)
button7.grid(row=0,column=1,sticky=N+S+E+W)






root.mainloop()
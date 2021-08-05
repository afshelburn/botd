import os

print("guage ui")

import tkinter as tk

from tkinter import *
import tkinter.font as tkFont

import tkinter.filedialog as fdialog
import tkinter.messagebox as messagebox



root = tk.Tk()

root.attributes('-zoomed',True)

#bigFont = tkFont.Font(family="Helvetica", weight="bold", size=200)

class Guage:
    def __init__(self, parent, title, sz=200):
        self.label = tk.StringVar(name=title + ".label", value=title)
        self.value = tk.IntVar(name=title + ".value",  value=0)
        self.label = Label(None, textvariable=self.label)
        self.title_frame = tk.LabelFrame(parent, labelwidget=self.label, padx=10, pady=5)
        
        bigFont = tkFont.Font(family="Helvetica", weight="bold", size=sz)
        
        self.valueWidget = tk.Entry(self.title_frame, textvariable=self.value, font=bigFont, width=3)
        
        self.value.set(20)
        
        self.valueWidget.grid(column=0,row=0)
        
    def grid(self, r, c, rows=1, cols=1):
        self.title_frame.grid(row=r,column=c,rowspan=rows,columnspan=cols)
        
speed = Guage(root, "Hello", 200)
speed.value.set(50)
speed.grid(0,1,rows=2,cols=1)

oil = Guage(root, "Oil Pressure", 60)
oil.value.set(40)
oil.grid(0,0)

temp = Guage(root, "Temperature", 60)
temp.value.set(185)
temp.grid(1,0)

volts = Guage(root, "Voltage", 60)
volts.value.set(13)
volts.grid(0,2)

fuel = Guage(root, "Fuel", 60)
fuel.value.set(4)
fuel.grid(1,2)

root.mainloop()





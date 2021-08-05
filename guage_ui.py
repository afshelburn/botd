import os
import vlc
import center_tk_window as centerTK

import tkinter as tk

from tkinter import *
import tkinter.font as tkFont

import tkinter.filedialog as fdialog
import tkinter.messagebox as messagebox

print("guage ui")

Instance = vlc.Instance(['--no-xlib'])
player = Instance.media_player_new()
Media = Instance.media_new('tcp://bot-rear:9072')

root = tk.Tk()

frm = tk.Toplevel(root, width=480, height=320)

#frame1 = tk.Frame(root, width=700, height=600)
#frame1.pack()

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
        
speed = Guage(root, "Speed", 200)
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
        
if __name__ == "__main__":

    import time
    import SN74HC165
    import pigpio
    
    def toggleBit(n, k):
         return (n^(1<<(k-1)))

    def adc_change(pin, level, ticks):
         #print("Pin " + str(pin) + " ADC Value = " + str(level))
         if pin == 0:
             speed.value.set(level)
         if pin == 1:
             oil.value.set(level)
         if pin == 2:
             temp.value.set(level)              
         if pin == 3:
             volts.value.set(level)
         if pin == 4:
             fuel.value.set(level)
             
    def cbf(piso, pin, level, tick):
        if level == 0:
            return
        print(pin, level, tick)
        btn = pin 
        print("Button " + str(btn))
        
        if frm.state() == 'normal':
            player.stop()
            frm.withdraw()
        else:
            display = tk.Frame(frm, bd=5)
            display.place(relwidth=1, relheight=1)

            player.set_xwindow(display.winfo_id())
            player.set_media(Media)
            player.play()
            frm.deiconify()
            centerTK.center(root, frm)
            
        
    pi = pigpio.pi()
    if not pi.connected:
        print("No pigpio!")
        exit()

    sr = SN74HC165.PISO(
              pi, SH_LD=16, OUTPUT_LATCH=26,
              SPI_device=SN74HC165.AUX_SPI, chips=2,
              reads_per_second=10, callback=cbf, adc_callback=adc_change, adc_channels=5)
    
    sr.set_adc_callback(adc_change)        
        


    root.mainloop()





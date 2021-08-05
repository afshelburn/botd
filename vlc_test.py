import vlc

from tkinter import *
import tkinter as tk

# root = Tk()
# root.geometry("380x480")
# root.resizable(width=False, height=False)
# 
# frame1 = LabelFrame(root, width=459, height=300, bd=5)
# frame1.grid(row=1, column=0, padx=10)

root = tk.Tk()

frame = tk.Frame(root, width=700, height=600)
frame.pack()

display = tk.Frame(frame, bd=5)
display.place(relwidth=1, relheight=1)

Instance = vlc.Instance(['--no-xlib', '--fullscreen'])
player = Instance.media_player_new()
Media = Instance.media_new('tcp://bot-rear:9072')
player.set_xwindow(display.winfo_id())
player.set_media(Media)
player.play()

root.mainloop()
#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#Name the window and set Geometry
root.title("Ganome's First Window")
root.geometry("300x200")

#Create a frame
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

#make a second frame
frame2 = ttk.Frame(root, padding="10 10 10 10")
frame2.pack(fill=tk.BOTH, expand=True)

#create buttons
button1 = ttk.Button(frame, text="Click Me!!")
button2 = ttk.Button(frame2, text="Don't Click Me!!")

button1.pack()
button2.pack()


root.mainloop()

# Program Name: assignment3.py
# Course: IT3883 Group 18
# Student Name: Enjie Jones
# Assignment Number: Lab 3
# Due Date: 2/23/2025
# Purpose: What does the program do (in a few sentences)?: Converts MPG to KM/L using a GUI. This app uses tkinter specifically.
# List Specific resources used to complete the assignment: Module 3-2 Gui powerpoint, https://www.geeksforgeeks.org/python-gui-tkinter/

import tkinter as tk
from tkinter import StringVar

#the program's main logic
def mpgtokml(event):
    try: #using a try / except so that an error isn't thrown with unexpected value. it will set the error to an empty string.
        mpg = float(mpg_var.get())
        kml = mpg * 0.425143707
        kml_var.set(f"{kml:0.3}")

    except ValueError:
        kml_var.set("")

root = tk.Tk() #creates the inital window
root.title("MPG to Km\L Converter")

mpg_var = StringVar() #stringvar so that the variables automatically update
kml_var = StringVar()

frame = tk.Frame(root, padx=25, pady=50) #adjust window frame size
frame.pack()

tk.Label(frame, text="Miles per Gallon (MPG):").grid(row=0, column=0) #creating the labels for both mpg and kml and placing them on a grid so they align properly
mpg_entry = tk.Entry(frame, textvariable=mpg_var)
mpg_entry.grid(row=0, column=2)
mpg_entry.bind("<KeyRelease>", mpgtokml) #important so that tkinter updates when a button is released, so we avoid the enter key
tk.Label(frame, text="Kilometers per Liter (Km\L):").grid(row=1, column=0)
kml_label = tk.Label(frame, textvariable=kml_var)
kml_label.grid(row=1, column=2)



root.mainloop() #runs the application

# importing required modules

from configparser import ConfigParser
from encodings import utf_8
from operator import imod
import requests
from tkinter import *
from tkinter import messagebox


# creation of object app

app = Tk()

# adding title to an app

app.title("Погода")

# adjusting windows size

app.geometry("300x300")

# add buttons, labels and text

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

Search_btn = Button(app, text= "Search weather", width = 12, command="search")
Search_btn.pack()

location_lbl = Label(app, text = "Location:", font = {"bold", 20})
location_lbl.pack()

temperature_lbl = Label(app, text ="")
temperature_lbl.pack()

weather_lbl = Label(app, text ="")
weather_lbl.pack()

app.mainloop()

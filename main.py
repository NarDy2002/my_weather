# importing required modules

# coding=utf-8

import json
import re
from configparser import ConfigParser
from encodings import utf_8
from operator import imod
from tkinter import *
from tkinter import messagebox
import requests

# extracting data from config file

config = ConfigParser()
config.read("config.ini")
api_key = config["default"]["api"]
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


def get_weather(city:str):
    """ 
    explicit fuction to get weather results
    """
    result = requests.get(url.format(city,api_key))

    if result:
        json = result.json()
       
        city = json["name"]
        country = json["sys"]
        temperature_kelvin = json["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15 
        weather = json["weather"][0]["main"]
    
        return city, country, temperature_kelvin, temperature_celsius, weather


def search():
    """
    Function to search sity
    """

    global city_text

    city = city_text.get()
    weather = get_weather(city)

    if weather is None:
        messagebox.showerror("Error", "Cannot find {}".format(city))
    else:
        location_lbl["text"] = "{}, {}".format(weather[0], weather[1])
        temperature_lbl["text"] = "{} degree Celsius".format(weather[3])
        weather_lbl["text"] = weather[4]


# creation of object app

app = Tk()

# adding title to an app

app.title("Weather")

# adjusting windows size

app.geometry("300x300")

# add buttons, labels and text

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

Search_btn = Button(app, text= "Search weather", width = 12, command=search)
Search_btn.pack()

location_lbl = Label(app, text = "Location:", font = {"bold", 20})
location_lbl.pack()

temperature_lbl = Label(app, text ="")
temperature_lbl.pack()

weather_lbl = Label(app, text ="")
weather_lbl.pack()

app.mainloop()
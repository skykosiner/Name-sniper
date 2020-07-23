import os
import time
import random
from bs4 import BeautifulSoup
import requests

print("Please enter your minecraft login")

UserName=input()
Password=input()

print("Welcome to minecraft name sniper")

print("What name would you like to snipe today")

name=input()

if (name == "360NOSCOPE"):
     print("No that is my name bitch")

print("starting the snipe")

# Get the timer from name mc depending on the name
source = requests.get("https://namemc.com/search?q=BlockBreaker6969").text
soup = BeautifulSoup(source, "lxml")
html = soup.find("html")
time = html.find("div", id="availability-time")


print(time)





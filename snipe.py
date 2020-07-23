import os
import time
import random
from bs4 import BeautifulSoup
import requests

print("non of your login deltais will ever be stored")

UserName=input("Enter you're minecraft username")
Password=input("Enter you're minecraft password")

print("Welcome to minecraft name sniper")

print("What name would you like to snipe today")

name=input()

if (name == "360NOSCOPE"):
     print("No that is my name bitch")

print("starting the snipe")

# Get the timer from name mc depending on the name
source = requests.get("https://namemc.com/search?q=BlockBreaker6969")
soup = BeautifulSoup(source, "lxml")
html = soup.find("html")
time = html.find("div", id="availability-time")


print(time)





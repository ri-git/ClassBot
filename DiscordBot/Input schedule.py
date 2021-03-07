from datetime import date
import schedule
#import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re
import schedule

mon = []
monstart = []
mondur = []
ncmon = (input("No. of classes on Monday: "))
ncmon = int(ncmon)
for i in range(ncmon):
    print("For class ",i+1)
    mon.append(input("Enter class name: "))
    monstart.append(input("Enter class start time: "))  #hour:min 
    mondur.append(input("Enter class duration in Seconds: "))
    if mon[i] == "COL100":
        schedule.every().monday.at(monstart[i]).do(opCOL100)
    elif mon[i] == "ELL101":
        schedule.every().monday.at(monstart[i]).do(opELL101)
    elif mon[i] == "MTL101":
        schedule.every().monday.at(monstart[i]).do(opMTL101B)
    else:
        print("Invalid Class Name")

tue = []
tuestart = []
tuedur = []
nctue = (input("No. of classes on Tuesday: "))
nctue = int(nctue)
for i in range(nctue):
    print("For class ",i+1)
    tue.append(input("Enter class name: "))
    tuestart.append(input("Enter class start time: "))  #hour:min 
    tuedur.append(input("Enter class duration in Seconds: "))
    if tue[i] == "COL100":
        schedule.every().tuesday.at(tuestart[i]).do(opCOL100)
    elif tue[i] == "ELL101":
        schedule.every().tuesday.at(tuestart[i]).do(opELL101)
    elif tue[i] == "MTL101":
        schedule.every().tuesday.at(tuestart[i]).do(opMTL101B)
    else:
        print("Invalid Class Name")

wed = []
wedstart = []
weddur = []
ncwed = (input("No. of classes on Wednesday: "))
ncwed = int(ncwed)
for i in range(ncwed):
    print("For class ",i+1)
    wed.append(input("Enter class name: "))
    wedstart.append(input("Enter class start time: "))  #hour:min 
    weddur.append(input("Enter class duration in Seconds: "))
    if wed[i] == "COL100":
        schedule.every().wednesday.at(wedstart[i]).do(opCOL100)
    elif wed[i] == "ELL101":
        schedule.every().wednesday.at(wedstart[i]).do(opELL101)
    elif wed[i] == "MTL101":
        schedule.every().wednesday.at(wedstart[i]).do(opMTL101B)
    else:
        print("Invalid Class Name")

thu = []
thustart = []
thudur = []
ncthu = (input("No. of classes on Thursday: "))
ncthu = int(ncthu)
for i in range(ncthu):
    print("For class ",i+1)
    thu.append(input("Enter class name: "))
    thustart.append(input("Enter class start time: "))  #hour:min 
    thudur.append(input("Enter class duration in Seconds: "))
    if thu[i] == "COL100":
        schedule.every().thursday.at(thustart[i]).do(opCOL100)
    elif thu[i] == "ELL101":
        schedule.every().thursday.at(thustart[i]).do(opELL101)
    elif thu[i] == "MTL101":
        schedule.every().thursday.at(thustart[i]).do(opMTL101B)
    else:
        print("Invalid Class Name")

fri = []
fristart = []
fridur = []
ncfri = (input("No. of classes on Friday: "))
ncfri = int(ncfri)
for i in range(ncfri):
    print("For class ",i+1)
    fri.append(input("Enter class name: "))
    fristart.append(input("Enter class start time (Hr(24):Min): "))  #hour:min 
    fridur.append(input("Enter class duration in Seconds: "))
    if fri[i] == "COL100":
        schedule.every().friday.at(fristart[i]).do(opCOL100)
    elif fri[i] == "ELL101":
        schedule.every().friday.at(fristart[i]).do(opELL101)
    elif fri[i] == "MTL101":
        schedule.every().friday.at(fristart[i]).do(opMTL101B)
    else:
        print("Invalid Class Name")


from datetime import date

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re



baseUrl = 'https://moodle.iitd.ac.in/login/index.php'
locationChromeDriver ='C:/Windows/chromedriver'

entryno = input("Enter Your Entry Number/Email: ")
pwd = input("Enter Your Moodle Password: ")
mclass= input("enter monday's class: ")
stime= input("enter start time: ")

drive = webdriver.Chrome(executable_path=locationChromeDriver)
drive.get(baseUrl)

search = drive.find_element_by_name('username')
search.send_keys(entryno)
spwd= drive.find_element_by_id('password')
spwd.send_keys(pwd)
#spwd.send_keys(Keys.RETURN)

text = drive.find_element_by_id('login').text
temp = re.findall(r'\d+', text)
res= list(map(int, temp))
if 'first' in text:
    ans = res[0]

if 'second' in text:
    ans = res[1]

if 'add' in text:
    ans = res[0] + res[1]

if 'subtract' in text:
    ans = res[0] - res[1]

cap = drive.find_element_by_name('valuepkg3')
cap.send_keys(ans)
cap.send_keys(Keys.RETURN)
# get element  after explicitly waiting for 10 seconds 
element = WebDriverWait(drive, 10).until( 
        EC.presence_of_element_located((By.LINK_TEXT, "3")) 
    ) 

# click the element  
element.click()
drive.find_element_by_xpath('//*[@id="course-info-container-10887"]/div/div[2]/h4/a').click()
drive.find_element_by_xpath('//*[@id="module-56927"]/div/div/div[2]/div/a/span').click()


day1 = []  # monday routine
day2 = []  # tuesday routine
day3 = []  # wednesday routine
day4 = []  # thursday routine
day5 = []  # friday routine

startclass = ["9:30",  ]  # starting time of classes in 24-hours format
endclass = ["11:00",  ]  # ending time of classes in 24-hours format
noc = 1
if date.today().weekday() == 5:
    print("MY BOT is checking MONDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        i=2
        for x in range(0, noc):
            if time.strftime('%H:%M') == stime:
                if mclass == "COL100":
                    drive.find_element_by_xpath('//*[@id="course-info-container-10887"]/div/div[2]/h4/a').click()
                    drive.find_element_by_xpath('//*[@id="module-56927"]/div/div/div[2]/div/a/span').click()
                print("MY BOT : Its time for the class")
                #classjoin(day1, x, endclass)
                continue



































import selenium
from selenium import webdriver
import time
import datetime
from datetime import date
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2,
                                      "profile.default_content_setting_values.media_stream_camera": 2})

emailid = input("Your Teams Email ID")
password = input("Your Teams Password")
filepath = r'../drivers/chromedriver'
day1 = []  # monday routine
day2 = []  # tuesday routine
day3 = []  # wednesday routine
day4 = []  # thursday routine
day5 = []  # friday routine
day6 = ["2002-COL100 INTRO. TO COMPUTER SCIENCE"]  # saturday routine
startclass = ["11:00",  ]  # starting time of classes in 24-hours format
endclass = ["12:00",  ]  # ending time of classes in 24-hours format
noc = 4

op = filepath#[:2].lower() + "//" + filepath[3:].replace('\\', '/') + "/chromedriver"
driver = webdriver.Chrome(options=opt, executable_path=op)

print("WELCOME TO MY BOT")
driver.get("http://teams.microsoft.com")
time.sleep(2)
#fbtn= driver.find_element_by_id("otherTileText")
#fbtn.click()
email = driver.find_element_by_id("i0116")
email.send_keys(emailid)
print("MY BOT: eMAIL ID entered")
time.sleep(2)
enter = driver.find_element_by_id("idSIButton9")
time.sleep(2)
enter.click()
time.sleep(2)
passwd = driver.find_element_by_id("i0118")
passwd.send_keys(password)
print("MY BOT: PASSWORD entered")
passbtn = driver.find_element_by_id("idSIButton9")
passbtn.click()
time.sleep(2)
confirmbtn = driver.find_element_by_id("idSIButton9")
confirmbtn.click()
print("MY BOT: Logged In to your Account. Loading TEAMS web app...")
time.sleep(2)
#usebtn = driver.find_element_by_link_text("Use the web app instead")
#usebtn.click()
print("MY BOT: TEAMS web app loaded")
time.sleep(5)
driver.find_element_by_id("app-bar-2a84919f-59d8-4441-a975-2a8c2643b741")
try:
    teambtn = driver.find_elements_by_css_selector('div.team-card')
    teambtn[0].click()
except:
    j = 0
    while j <= 1:
        teambtn = driver.find_elements_by_css_selector('div.team-card')
        if teambtn == None:
            time.sleep(2)
            continue
        elif teambtn != None:
            teambtn[0].click()
            print("MY BOT successfully entered inside your team.")
            break
time.sleep(3)


def classjoin(x, i, y):
    print("MY BOT: Searching the subject channel")
    z = x[i]
    channelbtn = driver.find_element_by_xpath("//a[@title=\'" + z + "\']")
    channelbtn.click()
    print("Channel Found")
    time.sleep(10)
    print("MY BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("MY BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    print("MY BOT is joining the meeting")
    d = 0
    while d <= 1:
        print("MY BOT is trying its best to join the meeting")
        time.sleep(2)
        conbtn = driver.find_element_by_css_selector('button.ts-btn-fluent-secondary-alternate')
        if conbtn == None:
            time.sleep(2)
            continue
        elif conbtn != None:
            conbtn.click()
            time.sleep(2)
            break
    joinbtn2 = driver.find_element_by_css_selector('button.join-btn')
    joinbtn2.click()
    time.sleep(5)
    print("MY BOT has joined the meeting")
    time.sleep(5)
    try:
        time.sleep(2)
        driver.find_element_by_id('callingButtons-showMoreBtn').click()
    except:
        u = 0
        while u <= 1:
            print("MY BOT: trying to press show more btn")
            showbtn = driver.find_element_by_id('callingButtons-showMoreBtn')
            if showbtn != None:
                driver.find_element_by_id('callingButtons-showMoreBtn').click()
                break
            elif showbtn == None:
                driver.find_element_by_css_selector('div.ts-calling-screen').click()
                continue
    try:
        driver.find_element_by_id('incoming-video-button').click()
        print("MY BOT: turned video off")
    except:
        o = 0
        while o <= 1:
            print('MY BOT: trying its best to turn off the video')
            inbtn = driver.find_element_by_id('incoming-video-button')
            if inbtn != None:
                driver.find_element_by_id('incoming-video-button').click()
                break
            elif inbtn == None:
                time.sleep(10)
                driver.find_element_by_css_selector('div.ts-calling-screen').click()
                driver.find_element_by_id('callingButtons-showMoreBtn').click()
                continue

    print("MY BOT has turned incoming video off")
    endtime = y[i]
    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == endtime:
            print("MY BOT is leaving the meeting")
            try:
                driver.find_element_by_css_selector('div.ts-calling-screen').click()
                driver.find_element_by_id('hangup-button').click()
                print("MY BOT has left the meeting")
            except:
                y = 0
                while y <= 1:
                    print("MY BOT is trying to leave the meeting")
                    exitbtn = driver.find_element_by_id('hangup-button')
                    if exitbtn == None:
                        driver.find_element_by_css_selector('div.ts-calling-screen').click()
                        continue
                    elif exitbtn != None:
                        driver.find_element_by_id('hangup-button').click()
                        driver.find_element_by_id('hangup-button').click()
                        break

            print("MY BOT left the class")
            break
        else:
            continue


if date.today().weekday() == 0:
    print("MY BOT is checking MONDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        for x in range(0, noc):
            if time.strftime('%H:%M') == startclass[x]:
                print("MY BOT : Its time for the class")
                classjoin(day1, x, endclass)
                continue

if date.today().weekday() == 1:
    print("MY BOT is checking TUESDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        for x in range(0, noc):
            if time.strftime('%H:%M') == startclass[x]:
                print("MY BOT : Its time for the class")
                classjoin(day2, x, endclass)
                continue

if date.today().weekday() == 2:
    print("MY BOT is checking WEDNESDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        for x in range(0, noc):
            if time.strftime('%H:%M') == startclass[x]:
                print("MY BOT : Its time for the class")
                classjoin(day3, x, endclass)
                continue

if date.today().weekday() == 3:
    print("MY BOT is checking THURSDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        for x in range(0, noc):
            if time.strftime('%H:%M') == startclass[x]:
                print("MY BOT : Its time for the class")
                classjoin(day4, x, endclass)
                continue

if date.today().weekday() == 4:
    print("MY BOT is checking FRIDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        for x in range(0, noc):
            if time.strftime('%H:%M') == startclass[x]:
                print("MY BOT : Its time for the class")
                classjoin(day5, x, endclass)
                continue

if date.today().weekday() == 5:
    print("MY BOT is checking SATURDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        for x in range(0, noc):
            if time.strftime('%H:%M') == startclass[x]:
                print("MY BOT : Its time for the class")
                classjoin(day6, x, endclass)
                continue

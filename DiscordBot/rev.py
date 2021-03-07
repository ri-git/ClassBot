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

import os

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')
baseUrl = 'https://moodle.iitd.ac.in/login/index.php'
locationChromeDriver ='C:\Program Files (x86)\chromedriver.exe'
# drive = webdriver.Chrome(executable_path=locationChromeDriver)
client = discord.Client()

# drive = webdriver.Chrome(executable_path=locationChromeDriver)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break            

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hi'):
        await message.channel.send('Hey, have a nice day!')

    if message.content.startswith('$class'):
        await message.channel.send('Enter your information in the terminal!') 
        
    #if message.content.startswith('$id'):
        #await message.channel.send('Enter your kerberos id!')
        #entryno=message.content

    #if message.content.startswith('$pwd'):
        #await message.channel.send('Enter your kerberos password!')
        #pwd= message.content    

        entryno = input("Enter Your Entry Number/Email: ")
        pwd = input("Enter Your Moodle Password: ")
        tempdur = 7200

        def opMoodle():
            drive = webdriver.Chrome(executable_path=locationChromeDriver)
            drive.get(baseUrl)

            search = drive.find_element_by_name('username')
            search.send_keys(entryno)
            spwd= drive.find_element_by_id('password')
            spwd.send_keys(pwd)

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
                page3 = WebDriverWait(drive, 10).until( 
                    EC.presence_of_element_located((By.LINK_TEXT, "3")) 
                )
                page3.click()

        def opCOL100():
            #opMoodle()
                drive = webdriver.Chrome(executable_path=locationChromeDriver)
                drive.get(baseUrl)

                search = drive.find_element_by_name('username')
                search.send_keys(entryno)
                spwd= drive.find_element_by_id('password')
                spwd.send_keys(pwd)

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
                #page3 = WebDriverWait(drive, 10).until( 
                    #EC.presence_of_element_located((By.LINK_TEXT, "3")) 
                #)
                page3= drive.find_element_by_link_text('3')
                page3.click()        
                drive.find_element_by_xpath('//*[@id="course-info-container-10887"]/div/div[2]/h4/a').click()
                drive.find_element_by_xpath('//*[@id="module-56927"]/div/div/div[2]/div/a/span').click()
                drive.find_element_by_xpath('/html/body/d1iv[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                time.sleep(tempdur)  #duration of a class?(seconds) 
                drive.switch_to.window(drive.window_handles[1])
                drive.close()
                drive.switch_to.window(drive.window_handles[0])
                drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                drive.find_element_by_link_text('3').click()
                #drive.close()

        def opELL101():
            #opMoodle()
                drive = webdriver.Chrome(executable_path=locationChromeDriver)
                drive.get(baseUrl)

                search = drive.find_element_by_name('username')
                search.send_keys(entryno)
                spwd= drive.find_element_by_id('password')
                spwd.send_keys(pwd)

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
                #page3 = WebDriverWait(drive, 10).until( 
                    #EC.presence_of_element_located((By.LINK_TEXT, "3")) 
                #)
                page3= drive.find_element_by_link_text('3')
                page3.click()
                drive.execute_script("scrollBy(0,-1000);")
                el = WebDriverWait(drive, 10).until( 
                        EC.presence_of_element_located((By.XPATH, '//*[@id="course-info-container-11053"]/div/div[2]/h4/a')) 
                    )
                el.click()
                drive.find_element_by_xpath('//*[@id="module-56737"]/div/div/div[2]/div/a/span').click()
                drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                time.sleep(tempdur)    #duration of a class?(seconds)
                drive.switch_to.window(drive.window_handles[1])
                drive.close()
                drive.switch_to.window(drive.window_handles[0])
                drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                drive.find_element_by_link_text('3').click()


        def opMTL101B():        
            # drive.get(baseUrl)
            #opMoodle()
                drive = webdriver.Chrome(executable_path=locationChromeDriver)
                drive.get(baseUrl)

                search = drive.find_element_by_name('username')
                search.send_keys(entryno)
                spwd= drive.find_element_by_id('password')
                spwd.send_keys(pwd)

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
                #page3 = WebDriverWait(drive, 10).until( 
                    #EC.presence_of_element_located((By.LINK_TEXT, "3")) 
                #)
                page3= drive.find_element_by_link_text('3')
                page3.click()
                drive.execute_script("scrollBy(0,-1500);")
                mt = WebDriverWait(drive, 10).until( 
                    EC.presence_of_element_located((By.XPATH, '//*[@id="course-info-container-11626"]/div/div[2]/h4/a')) 
                )
                mt.click()
                drive.find_element_by_xpath('//*[@id="module-59372"]/div/div/div[2]/div/a/span').click()
                drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                time.sleep(tempdur)    #duration of a class?(seconds)
                #driver.close()
                drive.switch_to.window(drive.window_handles[1])
                drive.close()
                drive.switch_to.window(drive.window_handles[0])
                drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                drive.find_element_by_link_text('3').click()

        mon = []
        monstart = []
        mondur = []
        ncmon = (input("No. of classes on Monday: "))
        ncmon = int(ncmon)
        for i in range(ncmon):
            print("For class ",i+1)
            mon.append(input("Enter class name: "))
            monstart.append(input("Enter class start time: "))  #hour:min 
            monlast = input("Enter class duration in Seconds: ")
            monlast = int(monlast) 
            mondur.append(monlast)
            tempdur = mondur[i]
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
            tuelast = input("Enter class duration in Seconds: ")
            tuelast = int(tuelast) 
            tuedur.append(tuelast)
            tempdur = tuedur[i]
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
            wedlast = input("Enter class duration in Seconds: ")
            wedlast = int(wedlast) 
            weddur.append(wedlast)
            tempdur = weddur[i]
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
            thulast = input("Enter class duration in Seconds: ")
            thulast = int(thulast) 
            thudur.append(thulast)
            tempdur = thudur[i]
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
            frilast = input("Enter class duration in Seconds: ")
            frilast = int(frilast) 
            fridur.append(frilast)
            tempdur = fridur[i]
            if fri[i] == "COL100":
                schedule.every().friday.at(fristart[i]).do(opCOL100)
            elif fri[i] == "ELL101":
                schedule.every().friday.at(fristart[i]).do(opELL101)
            elif fri[i] == "MTL101":
                schedule.every().friday.at(fristart[i]).do(opMTL101B)
            else:
                print("Invalid Class Name")



        # # schedule.every().sunday.at("18:42").do(opCOL100)
        # schedule.every().tuesday.at("18:43").do(opCOL100)
        # # schedule.every().tuesday.at("03:58").do(opMTL101B)
        # # schedule.every().wednesday.at("09:58").do(opELL101)
        # # schedule.every().wednesday.at("03:58").do(opMTL101B)
        # # schedule.every().thursday.at("09:28").do(opCOL100)
        # # schedule.every().friday.at("09:58").do(opELL101)
        # # schedule.every().friday.at("03:58").do(opMTL101B)

        while True: 

            # Checks whether a scheduled task is pending to run or not 
            schedule.run_pending() 
            time.sleep(1)


client.run(TOKEN)

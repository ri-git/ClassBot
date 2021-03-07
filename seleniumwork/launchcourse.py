from datetime import date       #"pip install datetime" in command line
from selenium import webdriver      #"pip install selenium" in command line
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import schedule     #"pip install schedule" in command line

#Download and install chrome and chromedriver

entryno = input("Enter Your Entry Number/Email: ") # If entry no. doesn't work try insti email "ID @ dept.uni"
pwd = input("Enter Your Moodle Password: ")

locationChromeDriver ='C:/drivers/chromedriver' #Change path to location of chromedriver in your system
drive = webdriver.Chrome(executable_path=locationChromeDriver)
       
def opMoodle():
    baseUrl = 'https://moodle.iitd.ac.in/login/index.php'
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
    opMoodle()
    drive.find_element_by_xpath('//*[@id="course-info-container-10887"]/div/div[2]/h4/a').click()
    drive.find_element_by_xpath('//*[@id="module-56927"]/div/div/div[2]/div/a/span').click()
    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
    time.sleep(7200)  #duration of a class?(seconds) 
    driver.close()

def opELL101():
    opMoodle()
    drive.execute_script("scrollBy(0,-1000);")
    el = WebDriverWait(drive, 10).until( 
            EC.presence_of_element_located((By.XPATH, '//*[@id="course-info-container-11053"]/div/div[2]/h4/a')) 
        )
    el.click()
    drive.find_element_by_xpath('//*[@id="module-56737"]/div/div/div[2]/div/a/span').click()
    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
    time.sleep(7200)    #duration of a class?(seconds)
    driver.close()

def opMTL101B():
    opMoodle()
    drive.find_element_by_xpath('//*[@id="course-info-container-11626"]/div/div[2]/h4/a').click()
    drive.find_element_by_xpath('//*[@id="module-59372"]/div/div/div[2]/div/a/span').click()
    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
    time.sleep(7200)    #duration of a class?(seconds)
    driver.close()


schedule.every().monday.at("09:28").do(opCOL100)
schedule.every().tuesday.at("09:58").do(opELL101)
schedule.every().tuesday.at("03:58").do(opMTL101B)
schedule.every().wednesday.at("09:58").do(opELL101)
schedule.every().wednesday.at("03:58").do(opMTL101B)
schedule.every().thursday.at("09:28").do(opCOL100)
schedule.every().friday.at("09:58").do(opELL101)
schedule.every().friday.at("03:58").do(opMTL101B)

while True: 
  
    # Checks whether a scheduled task is pending to run or not 
    schedule.run_pending() 
    time.sleep(1)



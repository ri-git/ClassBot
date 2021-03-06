from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re



baseUrl = 'https://moodle.iitd.ac.in/login/index.php'
locationChromeDriver ='../drivers/chromedriver'

entryno = input("enter your entry number: ")
pwd = input("enter your moodle password: ")

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
drive.find_element_by_link_text('3').click()
drive.find_element_by_xpath('//*[@id="course-info-container-10887"]/div/div[2]/h4/a').click()
drive.find_element_by_xpath('//*[@id="module-56927"]/div/div/div[2]/div/a/span').click()

































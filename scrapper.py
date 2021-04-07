#BeautifulSoup is not working for this website because it is identifying the python bot 
# from bs4 import BeautifulSoup
# import requests

# url = 'https://www.zocdoc.com/wl/stamfordcovid19vaccination/practice/64220?reason_visit=5243'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
# }
# response = requests.get (url, headers = headers)
# soup = BeautifulSoup (response.text,'html.parser')
# print (soup)

from selenium import webdriver

import pandas as pd
import time
import winsound

driver = webdriver.Chrome("D:\\Projects\\Covid-Appointment-Finder\\chromedriver_win32\\chromedriver.exe")
driver.get('https://www.zocdoc.com/wl/stamfordcovid19vaccination/patientvaccine')
print(driver.title)

python_button = driver.find_elements_by_xpath("//*[@id=\"modal-root\"]/div/div/div[2]/div/div/div/span/a")[0]
python_button.click()

time.sleep(3)  #sleep for 10 seconds so it cannot identify you as a bot
 
inputElement = driver.find_element_by_id('age-input')
inputElement.send_keys('36')

time.sleep(3) 
python_button = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[1]/button')[0]
python_button.click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[14]/div[1]/div[2]/div[2]/label/span[1]/input').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[14]/div[2]/div[2]/div[2]/label/span[1]/input').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[14]/div[3]/div[2]/div[2]/label/span[1]/input').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[14]/div[4]/div[2]/div[2]/label/span[1]/input').click()

python_button = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[14]/button')[0].click()

time.sleep(1)
python_button = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[17]/button')[0].click()

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

#x = driver.find_element_by_xpath('[data-test="timesgrid-no-availability-text"]')
time.sleep(3)
no_appointment1=driver.find_element_by_xpath('//*[@id="main"]/div/main/div[1]/div[1]/div/div/div[2]/article/section/div[3]/div[2]/div/div/div').text
no_appointment2=driver.find_element_by_xpath('//*[@id="main"]/div/main/div[1]/div[1]/div/div/div[2]/article/section/div[3]/div[2]/div/div/div').text

availability ='no upcoming appointments'
flag = False 

if ( not availability in no_appointment1.lower() ) :
    winsound.Beep(frequency, duration)
    flag = True

if  ( not availability in no_appointment2.lower() ):
    winsound.Beep(frequency, duration)
    flag = True
if flag == False:
    driver.quit()
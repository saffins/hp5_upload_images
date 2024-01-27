import random
import time

from helium import start_chrome
from helium import *
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from pynput.keyboard import Key, Controller


load_dotenv()
title = os.environ["title"]
alternativeText = os.environ["alternative"]
behaviourText = os.environ["behaviour"]

# CHANGE DESC VALUE BELOW AS PER YOUR NEED
desc = ["Excellent!","Awesome!","Wonderful!","Remarkable!","Good One!"]


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://trading.gopichandrakesan.com/wp-admin/')
driver.find_element(By.ID,'user_login').send_keys("TheMentalTrading")
driver.find_element(By.ID,'user_pass').send_keys("mentaltrading12345")
driver.find_element(By.ID,'wp-submit').click()
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//div[text()="H5P Content"]'))
    )
element.click()
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'(//a[text()="Add New"])[5]'))
    )
element.click()

outer = driver.find_element(By.CLASS_NAME, "h5p-editor-iframe")
driver.switch_to.frame(outer)
element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="hub-search-bar"]'))
    )

element.send_keys('memory game')

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[text()="Details"]'))
    )

element.click()
driver.switch_to.default_content()
driver.find_element(By.XPATH,'(//*[text()="Display Options"]/following-sibling::div//input)[2]').click()
driver.find_element(By.XPATH,'(//*[text()="Display Options"]/following-sibling::div//input)[3]').click()
btn = driver.find_element(By.XPATH,'(//*[text()="Display Options"]/following-sibling::div//input)[4]')
driver.execute_script("arguments[0].click();", btn)

outer = driver.find_element(By.CLASS_NAME, "h5p-editor-iframe")
driver.switch_to.frame(outer)
useBtn = driver.find_element(By.XPATH,'//*[text()="Use"]')
driver.execute_script("arguments[0].scrollIntoView();",
                      WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                        '//*[text()="Use"]'))))
useBtn.click()
element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,'//*[text()="Metadata"]'))
    )
driver.find_element(By.XPATH,'//input[@id="field-extratitle--1"]').send_keys(title)

def getNumOfFilesInFolder():
    dir_path = r'images'
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print('File count:', count)
    fin = count / 2


    if fin % 1 == 0:
        fin=int(fin)
    else:
        fin=fin

    return fin

numOfCards = getNumOfFilesInFolder()

if(numOfCards>2):
    numOfCards-=2
#for x in range((numOfCards)):
#C:\Users\alienware\PycharmProdriver.find_element(By.XPATH,'//*[text()="Add Card"]').click()
time.sleep(3)
from natsort import natsorted


filenames = os.listdir(r'images')
natsort_file_names = natsorted(filenames)

var = 0
fileCount=1
addCardCount=1
descincr=0

action = ActionChains(driver)

for i in range(numOfCards):
    if addCardCount>2:
        addcrd = driver.find_element(By.XPATH,'//*[text()="Add Card"]')
        driver.execute_script("arguments[0].scrollIntoView();",
                              WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                                '//*[text()="Add Card"]'))))
        addcrd.click()

    time.sleep(3)
    addCard = driver.find_element(By.XPATH, '//*[@class="h5p-vtabs"]/ol/li[' + str(addCardCount) + ']')
    driver.execute_script("arguments[0].scrollIntoView();",
                          WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                           '//*[@class="h5p-vtabs"]/ol/li[' + str(addCardCount) + ']'))))
    addCard.click()
    #action.move_to_element(addCard).click().perform()

    driver.find_element(By.XPATH,
                        '(//*[starts-with(text(),"Alternative text for Image")])[' + str(addCardCount) + ']/following::div[1]//following-sibling::input').send_keys(
        alternativeText)

    if(descincr>4):
        descincr=0


    for j in range(2):
        time.sleep(2)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'(//*[@class="file"]/a)['+str(fileCount)+']'))
        )
        driver.execute_script("arguments[0].scrollIntoView();",
                              WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                                '(//*[@class="file"]/a)['+str(fileCount)+']'))))

        element.click()
        #driver.find_element(By.XPATH,'(//*[@class="file"]/a)['+str(fileCount)+']').click()
        time.sleep(2)
        keyboard = Controller()
        keyboard.type(os.environ["imagePath"] + natsort_file_names[var])
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(3)
        var+=1
        fileCount+=2

    # last_height = driver.execute_script("return document.body.scrollHeight")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    descText = driver.find_element(By.XPATH,
                        '(//*[starts-with(text(),"An optional short")]/following-sibling::input)[' + str(addCardCount) + ']')

    driver.execute_script("arguments[0].scrollIntoView();",
                          WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '(//*[starts-with(text(),"An optional short")]/following-sibling::input)[' + str(addCardCount) + ']'))))

    descText.send_keys(desc[descincr])
    descincr += 1
    addCardCount+=1


behavourClick = driver.find_element(By.XPATH,'//*[text()="Behavioural settings"]')
driver.execute_script("arguments[0].scrollIntoView();",
                      WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                        '//*[text()="Behavioural settings"]'))))

behavourClick.click()

behavorTxt = driver.find_element(By.XPATH,'//*[starts-with(text(),"Setting this to a number greater")]/following-sibling::input')
driver.execute_script("arguments[0].scrollIntoView();",
                      WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                        '//*[starts-with(text(),"Setting this to a number greater")]/following-sibling::input'))))

behavorTxt.send_keys(10)

driver.switch_to.default_content()
#createBtn =
driver.execute_script("arguments[0].scrollIntoView();",
                      WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                        '//*[@value="Create"]'))))
driver.find_element(By.XPATH,'//*[@value="Create"]').click()




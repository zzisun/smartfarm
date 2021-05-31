from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time
from django.conf import settings

def background_posting():
    chrome_path = os.path.join(settings.BASE_DIR, "chromedriver")

    #add background option
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(executable_path=chrome_path, options=options)
    url = 'http://127.0.0.1:8000/twitter/share/'
    driver.get(url)
    time.sleep(1)
    driver.find_elements_by_css_selector('button.btn')[0].click()
    driver.find_element_by_id('username_or_email').send_keys('wbsl0427@gmail.com')
    driver.find_element_by_id('password').send_keys('dongjun1245!')
    driver.find_element_by_id('password').send_keys(Keys.ENTER)
    driver.find_element_by_id('twitter-share-btn').pause(3).click()
    driver.find_elements_by_css_selector('div.css-18t94o4')[0].click()

    #ActionChains(driver)\
    #    .click(action1)\
    #    .send_keys(action2, 'wbsl0427@gmail.com')\
    #    .send_keys(action3, 'dongjun1245!')\
    #    .send_keys(action4, Keys.ENTER)\
    #    .pause(3)\
    #    .click(action5)\
    #    .click(action6)\
    #    .perform()

    driver.quit()




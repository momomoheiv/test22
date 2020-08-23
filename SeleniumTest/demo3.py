from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://81.68.125.221:8080/ljindex')
driver.maximize_window()

login1 = ('xpath', '//*[@id="unlogin"]/div[1]/a')
username1 = ('id', 'username')
password1 = ('id', 'password')
login2 = ('id', 'userLogin')

find_element(driver, login1).click()
find_element(driver, username1).send_keys('zhangshisan')
find_element(driver, password1).send_keys('a1234567')
find_element(driver, login2).click()


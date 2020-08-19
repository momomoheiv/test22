from selenium import webdriver
from seleniumtools import find_element

d = webdriver.Chrome(executable_path='chromedriver.exe')
d.get('http://81.68.125.221:8080/ljindex')
d.maximize_window()

login1 = ('xpath', '//*[@id="unlogin"]/div[1]/a')
username1 = ('id', 'username')
password1 = ('id', 'password')
login2 = ('id', 'userLogin')

find_element(d, login1).click()
find_element(d, username1).send_keys('zhangshisan')
find_element(d, password1).send_keys('a1234567')
find_element(d, login2).click()


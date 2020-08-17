import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('http://81.68.125.221:8080/ljindex')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="unlogin"]/div[2]/a').click()

time.sleep(5)

driver.find_element_by_id('username').send_keys('zhangshisan')
driver.find_element_by_id('phonenum').send_keys('18956234758')
driver.find_element_by_id('password').send_keys('a1234567')
driver.find_element_by_id('confirpw').send_keys('a1234567')
driver.find_element_by_id('emailnum').send_keys('59486623@qq.com')
driver.find_element_by_id('userRegist').click()

time.sleep(5)
driver.quit()

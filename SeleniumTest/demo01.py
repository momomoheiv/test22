import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('http://81.68.125.221:9000/zentao')

driver.find_element_by_id('account').send_keys('liuyun')
driver.find_element_by_xpath('//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys('a12345678')
driver.find_element_by_id('submit').click()
driver.maximize_window()
time.sleep(5)
#标题断言
assert driver.title == '我的地盘 - 禅道'
print('测试成功')

# assert driver.current_url == 'http://81.68.125.221:9000/zentao/my/'

assert driver.find_element_by_xpath('//*[@id="userNav"]/li/a/span[1]').text == '流云'
driver.quit()

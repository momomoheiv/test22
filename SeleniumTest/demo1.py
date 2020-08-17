#导入selenium
from selenium import webdriver

#1.打开浏览器：实例化driver句柄（把柄），Chrome：大写的C
driver = webdriver.Chrome(executable_path='chromedriver.exe')
#2.打开网页
driver.get('https://www.baidu.com/')

driver.find_element_by_id('kw').send_keys('百度流量统计')
driver.find_element_by_id('su').click()
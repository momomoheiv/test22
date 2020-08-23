import unittest,time
from selenium import webdriver

class TestCaseLogin(unittest.TestCase):

    def test_01_login_sucess(self):

        driver = webdriver.Chrome(executable_path='driver\\chromedriver.exe')
        driver.get('http://81.68.125.221:8080/ljindex/')
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="unlogin"]/div[1]/a').click()
        time.sleep(5)
    
        driver.find_element_by_id('username').send_keys('zhangshisan')
        driver.find_element_by_id('password').send_keys('a1234567')
        driver.find_element_by_id('userLogin').click()
        time.sleep(10)
        # e =driver.find_element_by_xpath('//*[@id="articles"]/li[1]/div/div[1]')
        # assert e.text == '为什么要学习测试'
        assert driver.title == '测谈网'
if __name__ == '__main__':
    unittest.main()


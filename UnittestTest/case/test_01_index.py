import unittest,time
from selenium import webdriver

#用类来管理测试用例
class TestCaseIndex(unittest.TestCase):

    #方法test_数字_用例名称
    def test_01_tjjz(self):
        driver = webdriver.Chrome(executable_path='driver\\chromedriver.exe')
        driver.get('http://81.68.125.221:8080/ljindex/')
        time.sleep(3)

        e =driver.find_element_by_xpath('//*[@id="articles"]/li[1]/div/div[1]')
        assert e.text == '为什么要学习测试'

if __name__ == '__main__':
    unittest.main()
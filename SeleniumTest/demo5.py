import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.bilibili.com/")
driver.maximize_window()

driver.delete_all_cookies()
cookies = [{'domain': '.bilibili.com',  'httpOnly': False, 'name': 'bili_jct', 'path': '/', 'secure': False, 'value': 'f96ac2f5857f1675c1509db99f2dc285'}, 
{'domain': '.bilibili.com','httpOnly': True, 'name': 'SESSDATA', 'path': '/', 'secure': False, 'value': '792714f7%2C1613311289%2Cc9baa*81'}, 
{'domain': '.bilibili.com',  'httpOnly': False, 'name': 'DedeUserID', 'path': '/', 'secure': False, 'value': '50868812'}, 
{'domain': '.bilibili.com', 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': False, 'value': '8nqg19po'}, 
{'domain': 'www.bilibili.com', 'httpOnly': False, 'name': 'finger', 'path': '/', 'secure': False, 'value': '1571944565'}, 
{'domain': '.bilibili.com', 'httpOnly': False, 'name': 'buvid3', 'path': '/', 'secure': False, 'value': 'EC1528C4-13C6-41E5-9A65-FA2BDC4A182F143097infoc'},
{'domain': '.bilibili.com', 'httpOnly': False, 'name': 'DedeUserID__ckMd5', 'path': '/', 'secure': False, 'value': '2718ac9a12219f44'}, 
{'domain': '.bilibili.com', 'httpOnly': False, 'name': '_uuid', 'path': '/', 'secure': False, 'value': '2D539E9D-65F7-C698-880F-5F1FDF56DCFB66834infoc'}]


for a in cookies:
    print(a)
    driver.add_cookie(a)
driver.refresh()

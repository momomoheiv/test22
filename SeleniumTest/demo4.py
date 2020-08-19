import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://qk.mrhkj.com/admin/common/login.html")
driver.maximize_window()


# 1. 获取已经登录的cookie
# time.sleep(20)
# print(driver.get_cookies())

# 2. 删除之前原有的cookie，并添加已经登录的cookie
driver.delete_all_cookies() # 删除cookie
cookie = {'domain': 'qk.mrhkj.com', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'tsfihj01gf62880v0jbsh238rm'}
driver.add_cookie(cookie)   # 添加已经登录的cookie
driver.refresh()            # 刷新

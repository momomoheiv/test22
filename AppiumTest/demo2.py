from appium import webdriver   # 1.导入appium的webdriver
import time
from appiumtools import find_element
#打开app，获取手机的把柄
desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '7.1.2'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'PCT-AL10'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'uni.UNI06649C8'               # app的名字：
                                                            # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                            # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = 'io.dcloud.PandoraEntryActivity'              # 同上↑
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
desired_caps['noRest'] = True                               # 使用app缓存

# 去打开app，并且返回当前app的操作对象
#http://localhost:4723/wd/hub  appium desktop提供的
#desired_caps：手机、app信息的字典
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.find_element_by_accessibility_id('com.android.packageinstaller:id/permission_allow_button').click()
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]').click()
# time.sleep(5)
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("App")').click()
# driver.quit()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]').click()
time.sleep(5)
#没有办法定位元素，就去点击坐标
driver.tap([(354,1088)])
time.sleep(5)
# driver.implicitly_wait(5)
mu_btn = ('text', '我的')
find_element(driver,my_btn).click()

# driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
time.sleep(3)
username = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.widget.EditText'
driver.find_element_by_xpath(username).send_keys('yangjiasheng')
password = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]/android.view.View/android.widget.EditText'
driver.find_element_by_xpath(password).send_keys('a12345678')
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[8]').click()
time.sleep(5)

assert driver.find_elements_by_accessibility_id('通知公告').text == '通知公告'
print('登陆成功 ')

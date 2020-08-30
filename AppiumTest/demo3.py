# 导入模块
from wxpy import *
import requests
import json
# 初始化机器人，扫码登陆
bot = Bot()
robot = Bot()
def talk_robot(info='你好啊'):   #定义一个默认参数
    api_url = 'http://www.tuling123.com/openapi/api'  # 图灵接口url
    apikey = 'cfad22af9b524562a767b04e6a5f18a3'       # 注册图灵生成key 
    data = {'key': apikey, 'info': info}                                   
    r = requests.post(api_url, data=data).text
# response = json.loads(r)['text']
# return response
@robot.register()
def print_group_msg(msg):
    if msg.is_at:
        message = '{}'.format(msg.text)
        response = talk_robot(info=message)
    return response
embed()
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file, write_file
from utils.exceltools import read_excel

#测试登录成功
def test_01_login():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[2][2]
    d = eval(r[2][3]) #字符串转换成字典
    h = eval(r[2][4])
    res = requests.post(url=u, json=d, headers=h)
    assert res.status_code == r[2][6]
    assert res.json()['status'] == r[2][7]

#数据库查询
    sql = "select * from t_user where username = '{}'".format(d['username'])
    assert len(query(sql)) != 0 

    token = res.json()['data']['token']
    write_file('./conf/user_token.txt', token)

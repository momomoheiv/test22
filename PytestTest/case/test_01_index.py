import requests #用python做接口自动化测试
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.exceltools import read_excel

#获取首页轮播图
def test_01_lbt():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[0][2]
    res = requests.get(u)
    assert res.status_code == r[0][6]
    assert res.json()['status'] == r[0][7]

def test_02_question():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[1][2]
    res = requests.get(u)
    assert res.status_code == r[1][6]
    assert res.json()['status'] == r[1][7]
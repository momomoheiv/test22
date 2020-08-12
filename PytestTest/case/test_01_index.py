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

def test_02_questionlist():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[1][2]
    res = requests.get(u)
    assert res.status_code == r[1][6]
    assert res.json()['status'] == r[1][7]

def test_03_version():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[7][2]
    res = requests.get(u)
    assert res.status_code == r[7][6]
    assert res.json()['status'] == r[7][7]

def test_04_courselist():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[8][2]
    res = requests.get(u)
    
    assert res.status_code == r[8][6]
    assert res.json()['status'] == r[8][7]

def test_05_course():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[9][2]
    res = requests.get(u)
    assert res.status_code == r[9][6]
    assert res.json()['status'] == r[9][7]

def test_06_question():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[10][2]
    res = requests.get(u)
    assert res.status_code == r[10][6]
    assert res.json()['status'] == r[10][7]

def test_07_articlelist():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[11][2]
    res = requests.get(u)
    assert res.status_code == r[11][6]
    assert res.json()['status'] == r[11][7]

def test_08_article():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[12][2]
    res = requests.get(u)
    assert res.status_code == r[12][6]
    assert res.json()['status'] == r[12][7]

def test_09_inspirerlist():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[13][2]
    res = requests.get(u)
    assert res.status_code == r[13][6]
    assert res.json()['status'] == r[13][7]

def test_10_inspiere():
    r= read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[14][2]
    res = requests.get(u)
    assert res.status_code == r[14][6]
    assert res.json()['status'] == r[14][7]

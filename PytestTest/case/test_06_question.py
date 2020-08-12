import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file, write_file
from utils.exceltools import read_excel

def test_01_newquestion():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[16][2]
    d = eval(r[16][3]) #字符串转换成字典
    h = eval(r[16][4])
    res = requests.post(url=u, json=d, headers=h)
    assert res.status_code == r[16][6]
    assert res.json()['status'] == r[16][7]

    qid = res.json()['data']['questionid']
    write_file('./conf/user_qid.txt', str(qid))
    
    sql = "select * from t_questions where id = '{}'".format(read_file('./conf/user_qid.txt'))
    assert len(query(sql)) != 0

def test_02_updatequestion():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[17][2]
    d = eval(r[17][3]) #字符串转换成字典
    h = eval(r[17][4])
    res = requests.post(url=u, json=d, headers=h)
    assert res.status_code == r[17][6]
    assert res.json()['status'] == r[17][7]

    sql = 'select * from t_questions where id="{}" and title="{}"'.format(read_file('./conf/user_qid.txt'), d['title'])
    assert len(query(sql)) != 0

def test_03_deletequestion():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[18][2]
    d = eval(r[18][3]) #字符串转换成字典
    h = eval(r[18][4])
    res = requests.post(url=u, json=d, headers=h)
    assert res.status_code == r[18][6]
    assert res.json()['status'] == r[18][7]

    sql = 'select * from t_article where id="{}"'.format(read_file('./conf/user_qid.txt'))
    assert len(query(sql)) == 0
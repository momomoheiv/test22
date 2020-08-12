import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file, read_file 
from utils.exceltools import read_excel

def test_01_newarticle():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[4][2]
    d = eval(r[4][3])
    h = eval(r[4][4])
    res = requests.post(url=u,json=d,headers=h)
    assert res.status_code == r[4][6]
    assert res.json()['status'] == r[4][7]

    articleid = res.json()['data']['articleid']
    write_file('./conf/user_articleid.txt',str(articleid))
    
    
    sql = 'select * from t_article where id="{}"'.format(read_file('./conf/user_articleid.txt'))
    assert len(query(sql)) != 0

def test_02_updatearticle():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[5][2]
    d = eval(r[5][3])
    h = eval(r[5][4])
    res = requests.post(url=u,json=d,headers=h)
    assert res.status_code == r[5][6]
    assert res.json()['status'] == r[5][7]
    
    sql = 'select * from t_article where id="{}" and title="{}"'.format(read_file('./conf/user_articleid.txt'), d['title'])
    assert len(query(sql)) != 0

def test_03_deletearticle():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[6][2]
    d = eval(r[6][3])
    h = eval(r[6][4])
    res = requests.post(url=u,json=d,headers=h)
    assert res.status_code == r[6][6]
    assert res.json()['status'] == r[6][7]

    

    sql = 'select status from t_article where id="{}"'.format(read_file('./conf/user_articleid.txt'))
    assert query(sql)[0] == ('1',)
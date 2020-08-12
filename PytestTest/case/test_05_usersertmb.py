import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file, write_file
from utils.exceltools import read_excel

def test_01_mb():
    r = read_excel('data\\测谈网接口测试用例.xlsx','Sheet1')
    u = r[15][2]
    d = eval(r[15][3]) #字符串转换成字典
    h = eval(r[15][4])
    res = requests.post(url=u, json=d, headers=h)
    assert res.status_code == r[15][6]
    assert res.json()['status'] == r[15][7]

    

    sql = "select mb from t_user where username = 'huang255k'"
    assert len(query(sql)) != 0


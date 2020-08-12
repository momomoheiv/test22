import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file, read_file 

def test_01_newarticle():
    u = 'http://192.144.148.91:2333/article/new'
    d = {"title":"为什么要学测试", "content":"111", "tags":"测试1234", "brief":"介绍", "ximg":"dsfsdf.jpg" }
    h = {"Content-Type":"application/json", "token":read_file('./conf/user_token.txt')}
    res = requests.post(url=u,json=d,headers=h)
    assert res.status_code == 200 
    assert res.json()['status'] == 200 

    articleid = res.json()['data']['articleid']
    write_file('./conf/user_articleid.txt',str(articleid))
    user_articleid = read_file('./conf/user_articleid.txt')
    
    sql2 = 'select * from t_article where id="{}"'.format(user_articleid)
    assert len(query(sql2)) != 0



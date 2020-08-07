from filetools import read_file,write_file
# write_file('test.txt','aaa')
# res = read_file('test.txt')
# print(res)

import requests
from dbtools import query

u = 'http://192.144.148.91:2333/login'
d = {'username':'huang255k','password':'a12345783'}
r = requests.post(url=u, json=d)
# print(r.text)
#判断结果
assert r.status_code == 200  #判断状态码
assert r.json()['status'] == 200   #判断结果码 r是返回值  通过r.json()转换成dict格式
#查询数据库：接口的作用来查询
# sql = 'select * from t_user where username = "{}"'.format(d['username'])
# # print(query(sql))
# assert len(query(sql)) != 0

token = r.json()['data']['token']
write_file('user_token.txt', token)
user_token = read_file('user_token.txt')

# uid = str(r.json()['data']['articleid']
# write_file('user_articleid.txt', articleis)
# user_articleid = read_file('user_articleid.txt')

# u1 = 'http://192.144.148.91:2333/updateuserheadpic'
# d1 = {"ximg" :"头像.jpg"}
# h1 = {"Content-Type":"application/json", "token":user_token }
# res = requests.post(url=u1,json=d1,headers=h1)

# assert r.status_code == 200 
# assert r.json()['status'] == 200 

u2 = 'http://192.144.148.91:2333/article/new'
d2 = {"title":"为什么要学测试", "content":"111", "tags":"测试1254", "brief":"介绍", "ximg":"dsfsdf.jpg" }
h2 = {"Content-Type":"application/json", "token":user_token }
res = requests.post(url=u2,json=d2,headers=h2)
assert res.status_code == 200 
assert res.json()['status'] == 200 
print(res.text)

articleid = res.json()['data']['articleid']
write_file('user_articleid.txt',str(articleid))
user_articleid = read_file('user_articleid.txt')

sql2 = 'select * from t_article where id="{}"'.format(user_articleid)
assert len(query(sql2)) != 0
print('发表成功！')
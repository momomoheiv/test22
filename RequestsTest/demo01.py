import requests
from dbtools import query

#接口地址是字符串类型
# u = 'http://192.144.148.91:2333/getarticle?pagenum=1'
# r = requests.get(u)     #r是所得响应信息，requests。get(u)发送请求
# print(r.text)           #r.text:打印接口得返回值

u = 'http://192.144.148.91:2333/login'
d = {'username':'huang255k','password':'a12345783'}
r = requests.post(url=u, json=d)
print(r.text)
#判断结果
assert r.status_code == 200  #判断状态码
assert r.json()['status'] == 200   #判断结果码 r是返回值  通过r.json()转换成dict格式
#查询数据库：接口的作用来查询
sql = 'select * from t_user where username = "{}"'.format(d['username'])
print(query(sql))
assert len(query(sql)) != 0
print('测试通过')


# u = 'http://192.144.148.91:2333/get_title_img'
# r = requests.get(u)
# print(r.text)

# us = 'http://192.144.148.91:2333/regist'
# ds = {
# "username":"zhangshier", 
# "password":"a1234567", 
# "phone":"18212358234", 
# "email":"hh2h@163.com" 
# }
# rs = requests.post(url=us,json=ds)
# print(rs.text)


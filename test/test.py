# print('你好，浪晋学院')
# print(2333)
# print(2.333)
# print(True,False)
# print(())
# print({})
# print([])
# print(None)
# print(False and False)
# print(False and True)
# print(True or False)
# print(16%5)
# a = float(input('请输入数字：'))
# b = float(input('请输入数字2：'))
# print(a + b)

# a = input('请输入文章内容：')
# print('总输入字数：',len(a))

# print(False or  True)

# a = (1,2,3,'哈哈','嘻嘻')
# print(a[-3])
# b = (a,'哈哈',('嘻嘻','嘿嘿'))
# print(b)
# print(a.index('哈哈'))
# print(a.count('哈哈'))
# print(b[0])
# print(b[0][4])
# print(b[0].count(1))
# print(b[2].index('嘻嘻'))
'''
a = [1,2,3,'哈哈','嘻嘻']
a.append(3)
print(a)
a.extend('你吃了吗')
print(a)
a.extend([1,2])
print(a)
b = ['1,2',3]
a = a+b
print(a)
a.insert(5,'66')
print(a)
a.clear()
print(a)

b = [343,56,121,7,4,87]
b.sort()
print(b)
b.sort(reverse=True)
print(b)
b.remove(56)
print(b)
del b[0]
print(b)
print(b.pop(0))
print(b)
'''
# a = {'name':'张三','age':18,'address':'china','info':{},'sister':('小红','李四')}
# # print(a['sister'][1])
# print(a.get('360'))
# print(a['name'])
# print(a.keys())
# print(list(a.keys()))
# print(list(a.values()))
# print(a.items())
# print(list(a.items()))
# a.update(name='王武')
# print(a)
# a['age'] = 19
# print(a)
# a['sex'] = 'woman'
# print(a)
# del a['sex']
# print(a)

# a = {}
# name = input('请输入学生名字：')
# score = input('请输入考试成绩：')
# a[name] = score
# print(a)

# a = 10
# b = 11
# if a > b:
#     print('a大于b')
# else:
#     print('a不大于b')

# userinfo = {'username':'admin', 'password':'a1234567'}
'''
userinfo = {}
username = input('请输入注册账号：')
password = input('请输入注册密码：')
if len(username) > 5:
    if len(password) >8:
        userinfo['username'] = username
        userinfo['password'] = password
        print('注册成功')
    else:
        print('密码必须大于8位！')
else:
    print('账号必须大于5位！')
'''

# for i in range(0,5):
#     for j in range(0,5):
#         print('h',end=' ')
#     print()

'''
for i in [1,4,2,4]:
    print(2)

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end = ' ')
    print()
'''

# a = 1
# while a < 10:
#     print('今天ttt又被点名了')
#     a += 1

# for i in range(10):
#     if i&1:
#         continue
#     print(i)
'''
#作业第七题
a = [{"tom":98,"king":56,"lili":75}]
for i in a:
    i

A = []
B = []
for name in i:
    fine = {}
    fail = {}
    
    if  i.get(name) >= 60:
        fine[name] = i.get(name)
        A.append(fine)
       
    else:
        fail[name] = i.get(name)
        B.append(fail)
        
print('及格成绩：',A)
print('不及格成绩：',B)
       
#作业第八题

import time
count = 0 
while True:
    count += 1
    time.sleep(1)
    if count < 5:
        print('green...')
    elif count >= 5 and count < 10:
        print('red...')
    else:
        count = 0

#作业第九题
username = input()
'''

# a = '123:{}'.format(123)
# print(a)
# try:
#     a = [1,2,3]
#     print(a[9999])
#     print('none')
# except:
#     print('yes')
# print(2)   
a = [1,2,3]
print(a[9999])
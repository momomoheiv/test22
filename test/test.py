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

a = {}
name = input('请输入学生名字：')
score = input('请输入考试成绩：')
a[name] = score
print(a)

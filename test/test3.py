import pymysql
def query(sql):
    db = pymysql.connect(host='192.144.148.91', user='ljtest', password='123456', db='ljtestdb')
    cur = db.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    db.close()
    return res
#sql是字符串
#sql语句时之前所学的sql
# sql = 'select * from t_pymysql_account'
# res = query(sql)
# print(len(res))
def commit(sql):
    #1.连接数据库
    db = pymysql.connect(host='192.144.148.91', user='ljtest', password='123456', db='ljtestdb')
    #2.获取游标：查询窗口
    cur = db.cursor()
    #3.执行sql语句
    cur.execute(sql)
    #4.提交修改（事务）
    db.commit()
    db.close()
    
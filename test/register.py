from dbtools import commit
usernames = input('请输入注册账号：')
passwords = input('请输入注册密码：')
if 16 >= len(usernames) >= 5:
    if len(passwords) > 8:
        print('注册密码不能超过8位！')
    elif len(passwords) < 6:
        print('注册密码不能小于6位！')
    else:
        print('注册成功！')
        sql_commit = "insert into t_pymysql_account (username,password) values ('{}','{}')".format(usernames,passwords)
        commit(sql_commit)
elif len(usernames) > 16:
    print('注册账号不能超过16位！')
else:
    print('注册账号不能小于5位')




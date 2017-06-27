# -*- coding: utf-8 -*-
#################################################
# Theme: Process Data in MySQL
# Author : Alvin
# Date   : 2017-06-26
#################################################

import sys
import MySQLdb

# 1.连接数据库
try:
    conn = MySQLdb.connect(host='192.168.224.6', user='cloud_bi', passwd='cloud_bi@kd', db='testdm')
except Exception, e:
    print e
    sys.exit()

# 2.获取cursor游标对象来进行操作
curs = conn.cursor()

# 3.创建表
sql = "create table if not exists a_test(name varchar(128) primary key, age int(4))"
curs.execute(sql)
print "success create table a_test!"

# 4.插入单条数据
sql = "insert into a_test(name, age) values('%s', '%d')" % ("Allen", 23)
try:
    curs.execute(sql)
    conn.commit()  # 凡是insert,update,delete都要"提交事务commit()",否则数据库不会改变
    print "success insert a record!"
except Exception, e:
    conn.rollback()  # 异常必须回滚rollback()
    print e

# 5.插入多条数据
sql = "insert into a_test(name, age) values (%s, %s)"
param = (("Tom", 24), ("Alice", 25), ("Bob", 26))
try:
    curs.executemany(sql, param)  # 批量插入数据时必须用.executemany(sql)而不是.execute(sql),那是单条数据
    conn.commit()
    print "success insert many records!"
except Exception, e:
    conn.rollback()
    print e

# 6.删除数据
sql = 'delete from a_test where age = 26'
try:
    curs.execute(sql)
    conn.commit()
    print "success delete a record!"
except Exception, e:
    conn.commit()
    print e

# 7.更新数据
sql = 'update a_test set name = "Tony" where name = "Tom"'
try:
    curs.execute(sql)
    conn.commit()
    print "success update the table"
except Exception, e:
    conn.commit()
    print e

# 8.查询数据
sql = "select * from a_test"
curs.execute(sql)
allData = curs.fetchall()
# 如果有数据返回就循环输出,allData是个二维列表）
if allData:
    for data in allData:
        print data[0], data[1]  # 分别输出,结果为denny 23
        # print rec    # 也可以直接输出rec,不带下标rec[i], 结果为('denny', 23L)

# 9.关闭连接
curs.close()
conn.close()

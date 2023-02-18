"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/18
    Time: 16:08
"""
import pymysql

connect = pymysql.connect(host="82.156.74.26",
                          port=3306,
                          user='root',
                          password='Testfan#123',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor # 得到的结果是字典
                          )

# 得到一个游标对象，使用游标对象做数据库的基本操作
cursor = connect.cursor()   # 数据库的结果集

# 订单倒序排列，取前两个
cursor.execute("SELECT * FROM mtxshop_trade.es_order order by order_id desc limit 2;")
# 得到查询的所有结果
res = cursor.fetchall()
print(type(res), res)
cursor.close()
connect.close()

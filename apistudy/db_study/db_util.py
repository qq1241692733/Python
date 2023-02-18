"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/18
    Time: 16:43
"""
import time

import pymysql


class DBUtil:
    def __init__(self, host, user, password, port=3306):
        self.connect = pymysql.connect(host=host,
                                  port=port,
                                  user=user,
                                  password=password,
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor  # 得到的结果是字典
                                  )

    def select(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        self.connect.commit()
        cursor.close()
        return data

    def update(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()

    def close(self):
        if self.connect != None:
            self.connect.close()

if __name__ == '__main__':

    db_util = DBUtil(host="82.156.74.26",
                          user='root',
                          password='Testfan#123')

    for i in range(5):
        time.sleep(10)
        res = db_util.select("SELECT * FROM mtxshop_trade.es_order order by order_id desc limit 2;")
        print(res)
        print("====================")

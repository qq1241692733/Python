"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/17
    Time: 19:31
"""
import redis
# 创建连接池  decode_responses=False 取出来是字节对象
pool = redis.ConnectionPool(host='localhost',
                            port=6379,
                            decode_responses=True)
# 从连接池中拿到一个对象
r = redis.Redis(connection_pool=pool)

# 字符串操作
r.set('key1', 'value1', ex=30)
print(r.get('key1'))

# 哈希
r.hset('userinfo1', 'name', 'jhy')
r.hset('userinfo1', 'age', '18')
print(r.hgetall('userinfo1'))


# 列表
r.lpush('list1', '111', '222', '333')
print(r.lrange('list1', 0, -1))

# 集合
r.sadd('set1', 'data1', 'data2', 'data1')
print(r.smembers('set1'))

# 有序集合
r.zadd('sort_set', {'data1': 6, 'data2': 2, 'data3': 4})
print(r.zrange('sort_set', 0, -1, desc=True))

# 类型
print(r.type('sort_set'))


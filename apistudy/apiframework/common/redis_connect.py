"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/17
    Time: 19:53
"""
import javaobj
import redis


class RedisUtil:

    def __init__(self, host, pwd, port=6379, decode_responses=False):
        self.pool = redis.ConnectionPool(host=host,
                                         password=pwd,
                                         port=port,
                                         decode_responses=decode_responses)
        self.r = redis.Redis(connection_pool=self.pool)

    # 封装一个统一的数据获取方法
    def get(self, key):
        type = self.r.type(key).decode('utf-8')
        if type == 'string':
            return self.r.get(key)
        elif type == 'hash':
            return self.r.hgetall(key)
        elif type == 'list':
            return self.r.lrange(key, 0, -1)
        elif type == 'set':
            return self.r.smembers(key)
        elif type == 'zset':
            return self.r.zrange(key, 0, -1)
        else:
            raise Exception(f'{key}对应是数据类型不支持')

if __name__ == '__main__':
    redis_util = RedisUtil(host='82.156.74.26', pwd='mtx')
    # 购物车
    res = redis_util.get('{BUY_NOW_ORIGIN_DATA_PREFIX}_63459')
    print("redis中的缓存数据：", type(res), res)
    # res 是java序列化数据
    res_obj = javaobj.loads(res)
    print("反序列化后：", type(res_obj), res_obj)
    order_info = res_obj[0]
    # 获取类信息
    print(dir(order_info))
    # 获取
    print(order_info.__getattribute__('num'))
    print(order_info.__getattribute__('skuId'))
    print(order_info.__getattribute__('goodsName'))

    # res = redis_util.get('{CHECKOUT_PARAM_ID_PREFIX}_63459')
    # print(type(res), res)
    # # 打印发现 是个map，不能整体转换
    # for key, value in res.items():
    #     key1 = javaobj.loads(key)
    #     try:
    #         value1 = javaobj.loads(value)
    #         print(f'{key1}:{value1}')
    #     except:
    #         pass


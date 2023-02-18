"""
    Created with PyCharm.
    Description:
        uid  63459
    User: hong yaO
    Date: 2023-02-2023/2/15
    Time: 15:00
"""
import javaobj
import pytest

from redis_study.redis_connect import RedisUtil
from sdk.shop_apis import *

def setup_module():
    print("当前文件执行前，执行我")
    # buyer_login()

def teardown_module():
    print("当前文件执行完，执行我")

# 以下两个是针对方法的普通测试用例的，针对类中测试方法无效
def setup_function():
    print("每个函数执行前执行我")
def teardown_function():
    print("每个函数执行前执行我")

# 也可以放到方法的参数中，但是只会执行一次，在同一个类下
@pytest.mark.usefixtures('creat_goods')
class TestBuyNowApi:
    def setup_class(self):
        print("当前测试类执行前执行我")
    def teardown_class(self):
        print("当前测试类函数执行前执行我")

    def setup_method(self):
        print("当前类每个测试方法执行前执行我")
    def teardown_method(self):
        print("当前类每个测试方法执行前执行我")

    # 成功购买
    def test_buy_now_sccess(self, creat_goods, buyer_token):
        uid = buyer_token
        print(uid)
        print(f'这是重fixture里得到的商品数据：{creat_goods}')
        # buyer_login()
        # sku_id 不是商品id，而是商品的产品id
        resp = buy_now(sku_id=541)
        assert resp.status_code == 200
        print("相应信息：", resp.text)
        redis_util = RedisUtil(host='82.156.74.26', pwd='mtx')
        res = redis_util.get(f'{{BUY_NOW_ORIGIN_DATA_PREFIX}}_{uid}')
        res_obj = javaobj.loads(res)
        order_info = res_obj[0]
        assert order_info.__getattribute__('num') == 1
        assert order_info.__getattribute__('sku_id') == 541

    # sku_id 不存在
    def test_buy_now_skuid_not_exsits(self):
        # buyer_login()
        # sku_id 不是商品id，而是商品的产品id
        resp = buy_now(sku_id=51812265)
        assert resp.status_code == 500
        print("相应信息：", resp.text)
        assert resp.json()["message"] == "不合法"

    '''
    # sku_id 不存在
    # 已下架的 sku_id:542
    # 已删除的 sku_id:551
    # num超过库存
    # num 为 -1
    # num 为 0
    
    参数化：
        1.将数据抽离出来
        2.使用装饰器
    '''

    test_data = [
        #[sku_id, num, 状态码, data.code, data.message]
        ['sku_id 不存在', '4882626',     1, 500, '004', '不合法'],
        ['产品已下架', '542',         1, 500, '004', '不合法'],
        ['产品已删除', '551',         1, 500, '004', '不合法'],
        ['num超过库存', '541', 999999999, 500, '451', '商品库存已不足，不能购买。'],
        ['num为负数', '541',        -1, 400, '004', '购买数量必须大于0'],
        ['num为0', '541',         0, 400, '004', '购买数量必须大于0']
    ]

    # 异常的用例
    @pytest.mark.parametrize('casename, sku_id, num, except_status, except_data_code, except_data_message', test_data)
    def test_buy_now_exception(self, casename, sku_id, num, except_status, except_data_code, except_data_message):
        # buyer_login()
        # sku_id 不是商品id，而是商品的产品id
        resp = buy_now(sku_id=sku_id, num=num)
        print("相应信息：", resp.text)
        assert resp.status_code == except_status
        resp = resp.json()
        assert resp["code"] == except_data_code
        assert resp["message"] == except_data_message

class TestCreateTradeApi:
    # 对于创建交易接口，参数有两个，client 有5个有效值，way有两个有效值
    # 组合之后总的数据就说 5*2=10条，这种参数化的方式叫做笛卡尔积参数化
    # 笛卡尔积参数化适用于一个接口中的参数分别有多组有效值，他们需要组合
    client_data = ['PC', 'WAP', 'NATIVE', 'MINI']
    way_data = ['BUY_NOW', 'CART']
    @pytest.mark.parametrize('client', client_data) # 5
    @pytest.mark.parametrize('way', way_data)       # 2
    def test_create_trade(self, client, way):
        # buyer_login()
        # 创建交易接口的数据来源于立即购买接口个添加购物车接口
        # 如果way为BUY_NOW则需要先调用立即购买接口3.
        # 如果way是CART则需要先调用添加购物车接口
        if way == 'BUY_NOW':
            buy_now(sku_id=541)
        elif way == 'CART':
            # 优于购物车内可能有垃圾数据，所以先清空
            clear_carts()
            carts_add(sku_id=541)
        resp = create_trade(client=client, way=way)
        print(resp.text)
    # def test_create_trade(self):
    #     buyer_login()
    #     create_trade(client='WAP', way='BUY_NOW')

class TestCheckoutParamsApis:


    def test_create_trade(self, buyer_token, redis_util):
        uid = buyer_token
        print("*************", uid)
        resp = set_addressid(5416)
        assert resp.status_code == 200
        # 返回为空，去断言 redis 中的数据
        redis_util = RedisUtil(host='82.156.74.26', pwd='mtx')
        res = redis_util.get(f'{{CHECKOUT_PARAM_ID_PREFIX}}_{uid}')
        print(res)
        # 打印发现 是个map，不能整体转换
        for key, value in res.items():
            key1 = javaobj.loads(key)
            try:
                value1 = javaobj.loads(value)
                print(f'{key1}:{value1}')
            except:
                pass
            if key1 == 'address_id':
                assert value1 == 5416

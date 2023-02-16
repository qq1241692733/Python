"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/15
    Time: 15:00
"""
import pytest

from sdk.shop_apis import *


class TestBuyNowApi:
    # 成功购买
    def test_buy_now_sccess(self):
        buyer_login()
        # sku_id 不是商品id，而是商品的产品id
        resp = buy_now(sku_id=541)
        assert resp.status_code == 200
        print("相应信息：", resp.text)

    # sku_id 不存在
    def test_buy_now_skuid_not_exsits(self):
        buyer_login()
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
        ['4882626',     1, 500, '004', '不合法'],
        ['542',         1, 500, '004', '不合法'],
        ['551',         1, 500, '004', '不合法'],
        ['541', 999999999, 500, '451', '商品库存已不足，不能购买。'],
        ['541',        -1, 400, '004', '购买数量必须大于0'],
        ['541',         0, 400, '004', '购买数量必须大于0']
    ]

    # 异常的用例
    @pytest.mark.parametrize('sku_id, num, except_status, except_data_code, except_data_message', test_data)
    def test_buy_now_exception(self, sku_id, num, except_status, except_data_code, except_data_message):
        buyer_login()
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
        buyer_login()
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

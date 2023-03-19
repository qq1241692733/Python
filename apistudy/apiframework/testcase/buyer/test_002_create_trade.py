"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/28
    Time: 11:05
"""
import json

import jsonpath
import pytest

from api.buyer.cart_apis import *
from api.buyer.order_apis import CreateTradeApi


class TestCreateTrade:
    client_data = ['PC', 'WAP', 'NATIVE', 'MINI']
    way_data = ['BUY_NOW', 'CART']

    @pytest.mark.parametrize('client', client_data)  # 5
    @pytest.mark.parametrize('way', way_data)  # 2
    def test_create_trade(self, client, way):
        # buyer_login()
        # 创建交易接口的数据来源于立即购买接口个添加购物车接口
        # 如果way为BUY_NOW则需要先调用立即购买接口3.
        # 如果way是CART则需要先调用添加购物车接口
        if way == 'BUY_NOW':
            BuyNowApi(sku_id=541).send()
        elif way == 'CART':
            # 优于购物车内可能有垃圾数据，所以先清空
            DeleteCartApi().send()
            AddCartApi(sku_id=541).send()
        resp = CreateTradeApi(client=client, way=way).send()
        print(resp.text)
        assert resp.status_code == 200

        # 创建交易将订单数据存入数据库，那么如何校验数据的正确性
        # 从响应信息中得到 trad_sn，然后去数据库中去，看订单的 sku_id 和 num 是否和下单一致
        # trade_sn = resp.json()['trade_sn'] ，  trade_sn 和 sn 使用sn

        # jsonpath, 匹配到一定是列表，不配不到是false
        trade_sn = jsonpath.jsonpath(resp.json(), '$..sn')[0]
        # res = db_connect.select(f"SELECT * FROM mtxshop_trade.es_order where trade_sn={trade_sn};")
        # print(type(res), res)
        # items_json = res[0]['items_json']
        # items_json = json.loads(items_json)
        # db_sku_id = items_json[0]['sku_id']
        # db_num = items_json[0]['num']
        # print(res)
        # assert len(res) == 1
        # assert db_num == 1
        # assert db_sku_id == 541
        print("====================")

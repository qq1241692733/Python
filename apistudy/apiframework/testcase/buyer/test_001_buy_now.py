"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/20
    Time: 19:07
"""
import pytest

from api.buyer.cart_apis import BuyNowApi


class TestBuyNowApi:

    test_data = [
        #[sku_id, num, 状态码, data.code, data.message]
        ['sku_id 不存在', '4882626',     1, 500, '004', '不合法'],
        ['产品已下架',     '542',         1, 500, '004', '不合法'],
        ['产品已删除',     '551',         1, 500, '004', '不合法'],
        ['num超过库存',    '541', 999999999, 500, '451', '商品库存已不足，不能购买。'],
        ['num为负数',      '541',        -1, 400, '004', '购买数量必须大于0'],
        ['num为0',        '541',         0, 400, '004', '购买数量必须大于0']
    ]

    @pytest.mark.parametrize('casename, sku_id, num, except_status, except_data_code, except_data_message', test_data)
    def test_buy_now_exception(self, casename, sku_id, num, except_status, except_data_code, except_data_message):
        # 最后这个aa，是主动调用fixture函数aa
        # 调用立即购买接口，传入测试数据
        resp = BuyNowApi(sku_id=sku_id, num=num).send()
        print("相应信息：", resp.text)
        assert resp.status_code == except_status
        resp = resp.json()
        assert resp["code"] == except_data_code
        assert resp["message"] == except_data_message

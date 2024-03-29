"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/19
    Time: 21:56
"""
from api.baseapi import BaseBuyerApi
from api.buyer.login_apis import BuyerLoginApi


class BuyNowApi(BaseBuyerApi):

    def __init__(self, sku_id, num=1):
        super(BuyNowApi, self).__init__()
        self.url = f'{self.host}/trade/carts/buy'
        self.method = 'post'
        self.data = {
            "sku_id": sku_id,
            "num": num,
            'activity_id': ''
        }

class AddCartApi(BaseBuyerApi):

    def __init__(self,sku_id,num=1):
        super().__init__()
        self.url = f'{self.host}/trade/carts'
        self.method = 'post'
        self.data = {
        # 注意sku_id并不是商品id，而是商品id所对应的sku_id
        # 可以通过查mtxshop_goods库获取，SELECT * FROM `es_goods_sku` where goods_id=21640;
            'sku_id': sku_id,
            'num': num,
            'activity_id': ''
        }
class DeleteCartApi(BaseBuyerApi):
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/trade/carts'
        self.method = 'delete'
if __name__ == '__main__':
    buyer_login_api = BuyerLoginApi(username="hongyao", password="e10adc3949ba59abbe56e057f20f883e")
    resp = buyer_login_api.send().json()
    print(resp)
    BaseBuyerApi.buyer_token = resp['access_token']
    resp = BuyNowApi(sku_id=541).send()
    print(resp.status_code)

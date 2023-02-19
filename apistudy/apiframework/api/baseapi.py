"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/19
    Time: 22:00
"""
from common.clinet import RequestClient


class BaseBuyerApi(RequestClient):

    buyer_token = ''

    def __init__(self):
        super(BaseBuyerApi, self).__init__()
        self.host = 'http://www.mtxshop.com:7002'
        self.headers = {
            "Authorization": BaseBuyerApi.buyer_token
        }


class BaseSellerApi(RequestClient):

    buyer_token = ''

    def __init__(self):
        super(BaseSellerApi, self).__init__()
        self.url = 'http://www.mtxshop.com:7003'
        self.headers = {
            "Authorization": BaseBuyerApi.buyer_token
        }



class BaseManagerApi(RequestClient):

    buyer_token = ''

    def __init__(self):
        super(BaseManagerApi, self).__init__()
        self.url = 'http://www.mtxshop.com:7004'
        self.headers = {
            "Authorization": BaseBuyerApi.buyer_token
        }


class BaseBaseBasicApiApi(RequestClient):

    buyer_token = ''

    def __init__(self):
        super(BaseBaseBasicApiApi, self).__init__()
        self.url = 'http://www.mtxshop.com:7002'
        self.headers = {
            "Authorization": BaseBuyerApi.buyer_token
        }


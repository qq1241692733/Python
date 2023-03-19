# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : order_apis.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-09-15 22:02
# @Copyright: 北京码同学
from api.baseapi import BaseBuyerApi


class CreateTradeApi(BaseBuyerApi):

    def __init__(self,client='PC',way='BUY_NOW'):
        super().__init__()
        self.url = f'{self.host}/trade/create'
        self.method = 'post'
        self.data = {
            'client':client,
            'way':way
        }
class SearchOrderApi(BaseBuyerApi):

    def __init__(self,order_status='',key_words='',start_time='',endtime=''):
        super().__init__()
        self.url = f'{self.host}/trade/orders'
        self.method = 'get'
        self.params = {
            'page_no':1,
            'page_size':5,
            'order_status':order_status,
            'key_words':key_words,
            'start_time':start_time,
            'endtime':endtime
        }

class CancelOrderApi(BaseBuyerApi):

    def __init__(self,order_sn,reason='没啥原因就是不想要了'):
        super().__init__()
        self.url = f'{self.host}/trade/orders/{order_sn}/cancel'
        self.method = 'post'
        self.data = {
            'reason':reason,
        }
class OrderRogApi(BaseBuyerApi):

    def __init__(self,order_sn):
        super().__init__()
        self.url = f'{self.host}/trade/orders/{order_sn}/rog'
        self.method = 'post'
class ReturnGoodsApi(BaseBuyerApi):

    def __init__(self,order_sn,sku_id,region):
        super().__init__()
        self.url = f'{self.host}/after-sales/apply/return/goods'
        self.method = 'post'
        self.data = {
            'service_type': 'RETURN_GOODS',
            'images': 'http://www.mtxshop.com:7000/statics/attachment/normal/2022/7/24/9/58263306.png',
            'return_num': 1,
            'ship_addr': '北京霍营',
            'ship_name': '沙陌',
            'ship_mobile': '18729399607',
            'account_type': 'BANKTRANSFER',
            'bank_name': '沙陌银行',
            'bank_deposit_name': '北京分行',
            'bank_account_name': '沙陌',
            'bank_account_number': '7272634623464',
            'reason': '发错货',
            'problem_desc': '不想说啥了，就想退',
            'order_sn': order_sn,
            'sku_id': sku_id,
            'apply_vouchers': '',
            'region': region,
        }


"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/15
    Time: 12:22
"""

import requests

# 设置收货地址
def set_addressid(id):
    url = f'http://www.mtxshop.com:7002/trade/checkout-params/address-id/{id}'
    header = {
        'Authorization': buyer_token
    }
    data = {
        "address_id": id
    }
    resq = requests.post(url=url, headers=header, data=data)
    return resq

# 设置交易方式  支付类型 在线支付：ONLINE，货到付款：COD
def pay_type(payment_type="COD"):
    url = '/trade/checkout-params/payment-type'
    header = {
        'Authorization': buyer_token
    }
    data = {
        "payment_type": payment_type
    }
    resq = requests.post(url=url, headers=header, data=data)
    return resq

# 查询会员订单列表
def query_orders_list(goods_name, key_words, page_no, page_size, start_time, end_time, order_status=1):
    url = '/trade/orders'
    header = {
        'Authorization': buyer_token
    }
    params = {
        "goods_name": goods_name,
        "key_words": key_words,
        "order_status": order_status,
        "page_no": page_no,
        "page_size": page_size,
        "start_time": start_time,
        "end_time": end_time
    }
    resq = requests.get(url=url, headers=header, params=params)
    return resq

# 取消订单
def cancel_order(order_sn, reason):
    url = f'/trade/orders/{order_sn}/cancel'
    header = {
        'Authorization': buyer_token
    }
    data = {
        "order_sn ": order_sn,
        "reason": reason
    }
    resq = requests.post(url=url, headers=header, data=data)
    return resq


# 确认收获
def confirm_received_goods(order_sn):
    url = f'/trade/orders/{order_sn}/rog'
    header = {
        'Authorization': buyer_token
    }
    data = {
        "order_sn ": order_sn,
    }
    resq = requests.post(url=url, headers=header, data=data)
    return resq

# 订单申请售后服务 -- 退货申请
def request_refund(apply_vouchers, bank_account_name, bank_account_number, bank_deposit_name,
                   bank_name, order_sn, problem_desc, reason, return_account, ship_addr, ship_mobile, ship_name,
                   sku_id=0, return_num=0, account_type="ALIPAY"):
    url = f'/after-sales/apply/return/goods'
    header = {
        'Authorization': buyer_token
    }
    data = {
        "account_type": account_type,
        "apply_vouchers": apply_vouchers,
        "bank_account_name": bank_account_name,
        "bank_account_number": bank_account_number,
        "bank_deposit_name": bank_deposit_name,
        "bank_name": bank_name,
        "images": [
            "string"
            ],
        "order_sn": order_sn,
        "problem_desc": problem_desc,
        "reason": reason,
        "return_account": return_account,
        "return_num": return_num,
        "ship_addr": ship_addr,
        "ship_mobile": ship_mobile,
        "ship_name": ship_name,
        "sku_id": sku_id
    }
    resq = requests.post(url=url, headers=header, data=data)
    return resq

# 提交评论

# 清空购物车接口
def clear_carts():
    url = 'http://www.mtxshop.com:7002/trade/create'
    header = {
        'Authorization': buyer_token
    }
    resq = requests.delete(url=url, headers=header)
    return resq

# 添加交易
def create_trade(client='PC', way= 'BUY_NOW'):
    url = 'http://www.mtxshop.com:7002/trade/create'
    header = {
        'Authorization': buyer_token
    }

    data = {
        'client': client,
        'way': way
    }
    resq = requests.post(url=url, data=data, headers=header)
    return resq

# 立即购买
def buy_now(sku_id, num=1, activity_id=""):
    url = 'http://www.mtxshop.com:7002/trade/carts/buy'
    header = {
        'Authorization': buyer_token
    }

    data = {
        'sku_id': sku_id,
        'num': num,
        'activity_id': activity_id
    }
    resq = requests.post(url=url, data=data, headers=header)
    return resq

# 添加到购物车
def carts_add(sku_id, num=1, activity_id=""):
    url = 'http://www.mtxshop.com:7002/trade/carts'
    header = {
        'Authorization': buyer_token
    }

    data = {
        'sku_id': sku_id,
        'num': num,
        'activity_id': activity_id
    }
    resq = requests.post(url=url, data=data, headers=header)
    return resq.json()


session = requests.session()
# 商城买家登录接口
# 表单参数的post接口调用
def buyer_login():
    url = 'http://www.mtxshop.com:7002/passport/login'
    headers = {
        "Authorization":""
    }
    # 表单参数使用data表示
    data = {
        "username":"hongyao",
        "password":"e10adc3949ba59abbe56e057f20f883e",
        "captcha":"1512",
        "uuid":"asdjhsadhahsddhds"
    }
    # 发起调用
    resp = session.request(method='post', url=url, data=data, headers=headers)
    # 以json格式数据的方式获取，得到的应该一个字典
    resp_json = resp.json()
    # 解析响应数据获取access_token
    global buyer_token
    buyer_token = resp_json['access_token']
    return resp

# json格式数据
# 以买家提交评论接口为例子
def buyer_comment():
    url = 'http://www.mtxshop.com:7002/members/comments'
    headers = {
        "Authorization": buyer_token
    }
    # json参数
    json = {
      "comments": [
            {
              "content": "这是评论内容",
              "grade": "good",
              "images": [
                ""
              ],
              "sku_id": 543
            }
          ],
      "delivery_score": 5,
      "description_score": 5,
      "order_sn": "2873773273",
      "service_score": 5
    }
    resp = session.request(method='post', url=url, json=json, headers=headers)
    return resp


if __name__ == '__main__':
    buyer_login()
    buyer_comment()


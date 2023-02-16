# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : token_study.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/2/7 22:02
# @Copyright: 北京码同学


import requests


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
        "username":"shamo",
        "password":"0659c7992e268962384eb17fafe88364",
        "captcha":"1512",
        "uuid":"asdjhsadhahsddhds"
    }
    # 发起调用
    resp = session.request(method='post',url=url,data=data,headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码:{status_code}')
    # 响应报文获取
    # 以纯字符串类型的方式得到
    text = resp.text
    print(f'字符串类型的响应报文:{text}')
    # 以json格式数据的方式获取，得到的应该一个字典
    resp_json = resp.json()
    print(f"json格式数据：{resp_json}")
    # 解析响应数据获取access_token
    global buyer_token
    buyer_token = resp_json['access_token']


# json格式数据
# 以买家提交评论接口为例子
def buyer_comment():
    url = 'http://www.mtxshop.com:7002/members/comments'
    headers = {
        "Authorization":buyer_token
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
    # 发起接口调用
    resp = session.request(method='post',url=url,json=json,headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码:{status_code}')
    # 响应报文获取
    # 以纯字符串类型的方式得到
    text = resp.text
    print(f'字符串类型的响应报文:{text}')
    # 以json格式数据的方式获取，得到的应该一个字典
    resp_json = resp.json()
    print(f"json格式数据：{resp_json}")
if __name__ == '__main__':
    buyer_login()
    buyer_comment()
"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/8
    Time: 20:37
"""
import requests

def log(resp):
    # 获取相应状态码
    status_code = resp.status_code
    print(f'status_code:{status_code}')
    # 响应报文
    # 字符串格式
    text = resp.text
    print(f'text字符串类型报文:{text}')
    # json 格式
    json = resp.json()
    print(f'json格式：{json}')

def get_article():
    url = 'http://82.156.74.26:7000/pages/articles/1212'

    resp = requests.get(url=url)
    # 获取相应状态码
    status_code = resp.status_code
    print(f'status_code:{status_code}')
    # 响应报文
    # 字符串格式
    text = resp.text
    print(f'text:{text}')
    # json 格式
    json = resp.json()
    print()

def article_categories():
    url = 'http://82.156.74.26:7000/pages/article-categories'
    params = {
        'category_type': 'OTHER'
    }
    resp = requests.get(url=url, params=params)
    log(resp)


def login():
    url = 'http://82.156.74.26:7000/passport/login'
    header = {
        "Authorization": ""
    }
    data = {
        "username": 'admin',
        "password": '0659c7992e268962384eb17fafe88364',
        "captcha": '1512',
        "uuid": 'fhniamvgrw91tr'
    }
    resp = requests.post(url=url, data=data, headers=header)
    log(resp)

# 买家提交评论
def buy_comment():
    url = '/passport/login'
    header = {
        "Authorization": ""
    }
    data = {
        "username": 'd',
        "password": 'v',
        "captcha": '1512',
        "uuid": 'fhniamvgrw91tr'
    }
    resp = requests.post(url=url, data=data, headers=header)
    log(resp)

if __name__ == '__main__':
    #get_article()
    article_categories()
    login()


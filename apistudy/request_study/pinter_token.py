"""
    Created with PyCharm.
    Description:
        token 使用全局变量，session 使用是自带的类
    User: hong yaO
    Date: 2023-02-2023/2/9
    Time: 21:33
"""

import requests

def case_login():
    url = 'http://82.156.74.26:9088/pinter/bank/api/login2'

    params = {
        "userName": "admin",
        "password": "1234"
    }
    #resp = requests.post(url=url, params=params)
    resp = requests.post(url=url, params=params)
    global testfan_token
    global token
    token = resp.json()['data']
    print(resp.json())

def case_query():
    url = 'http://82.156.74.26:9088/pinter/bank/api/query2'
    header = {
        "Authorization": token
    }
    params = {
        "testfan-token": "admin",
    }
    resp = requests.get(url=url, params=params, headers=header)
    print(resp.json())

if __name__ == '__main__':
    case_login()
    case_query()

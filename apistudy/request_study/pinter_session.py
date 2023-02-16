"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/9
    Time: 20:55
"""
import requests

session = requests.session()

def case_login():
    url = 'http://82.156.74.26:9088/pinter/bank/api/login'

    params = {
        "userName": "admin",
        "password": "1234"
    }
    #resp = requests.post(url=url, params=params)
    resp = session.post(url=url, params=params)
    print(resp.json())

def case_query():
    url = 'http://82.156.74.26:9088/pinter/bank/api/query'

    params = {
        "userName": "admin",
    }
    resp = session.get(url=url, params=params)
    print(resp.json())

if __name__ == '__main__':
    case_login()
    case_query()

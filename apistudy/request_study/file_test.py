"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/15
    Time: 10:48
"""
import requests


def upload():
    url = "http://82.156.74.26:7000/uploaders"

    params = {
        "scene": "goods"
    }
    file = {
        "file": ('tupian.png', open(file=r"C:\Users\hong yaO\Desktop\tupian.png", mode='rb'), 'image/png')
    }
    resp = requests.session().request(method='post', url=url, params=params, files=file)
    print(resp.text)


if __name__ == '__main__':
    upload()

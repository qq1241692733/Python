"""
    Created with PyCharm.
    Description:
        所有接口封装的基类
    User: hong yaO
    Date: 2023-02-2023/2/19
    Time: 15:56
"""
import requests


class RequestClient:
    # 所有接口的全局对象
    session = requests.Session()

    def __init__(self):
        self.url = None
        self.method = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.files = None
        self.resp = None

    def send(self, **kwargs):
        # url 和 method 为空, 或者说附默认值
        if 'url' not in kwargs:
            kwargs['url'] = self.url
        if 'method' not in kwargs:
            kwargs['method'] = self.method
        if 'headers' not in kwargs:
            kwargs['headers'] = self.headers
        if 'params' not in kwargs:
            kwargs['params'] = self.params
        if 'data' not in kwargs:
            kwargs['data'] = self.data
        if 'json' not in kwargs:
            kwargs['json'] = self.json
        if 'files' not in kwargs:
            kwargs['files'] = self.files
        return RequestClient.session.request(**kwargs)

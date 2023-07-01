"""
    Created with PyCharm.
    Description:
        所有接口封装的基类
    User: hong yaO
    Date: 2023-02-2023/2/19
    Time: 15:56
"""
import requests
# import grpc
from common.encry_decry import AesEncrypt
from common.file_load import load_yaml_file
from common.logger import GetLogger

from common.logger import GetLogger


class RequestClient:
    # 所有接口的全局对象
    session = requests.Session()

    def __init__(self):
        # logger 的初始化在 fix 中 这里直接用
        self.logger = GetLogger.logger
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
        # 接口请求数据日志收集
        for key, value in kwargs.items():
            self.logger.info(f'接口的{key}是:{value}')
        try:
            self.resp = RequestClient.session.request(**kwargs)
            self.logger.info(f'接口响应状态码是:{self.resp.status_code}')
            self.logger.info(f'接口响应信息是:{self.resp.text}')
        except BaseException as e:
            self.logger.exception('接口发起报错')
            raise BaseException(f'接口发起报错:{e}')  # 这句抛出异常，终止执行

        return RequestClient.session.request(**kwargs)


# class GrpcChannel:
#     channel=None
#     def __init__(self):
#         self.host = load_yaml_file('/config/grpc.yml')['host']
#         GrpcChannel.channel = grpc.insecure_channel(self.host)


class BaseDubbo:

    def __init__(self):
        self.host = load_yaml_file('/config/dubbo.yml')['host']
        self.dubbo_version = load_yaml_file('/config/dubbo.yml')['dubbo_version']
        self.version  =load_yaml_file('/config/dubbo.yml')['version']
    def send(self,method,*args):
        res = self.service.call(method,args=args)
        return res

class WebsocketClient:

    def __init__(self):
        self.host = load_yaml_file('/config/websocket.yml')['host']
        self.logger = GetLogger.logger

    def send(self,params):
        try:
            self.ws.send(params)
            self.logger.info(f'发送数据成功:{params}')
        except:
            self.logger.exception('发送数据失败')
    def recv(self):
        try:
            res = self.ws.recv()
            self.logger.info(f'数据接收成功:{res}')
            return res
        except:
            self.logger.exception('接收数据失败')
            return ''

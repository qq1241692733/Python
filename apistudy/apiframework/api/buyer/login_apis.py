"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/19
    Time: 16:22
"""
from api.baseapi import BaseBuyerApi


class BuyerLoginApi(BaseBuyerApi):
    
    def __init__(self, username, password):
        super(BuyerLoginApi, self).__init__()
        self.url = f'{self.host}/passport/login'
        self.method = 'post'
        self.data = {
            "username": username,
            "password": password,
            "captcha": "1512",
            "uuid": "asdjhsadhahsddhds"
        }




if __name__ == '__main__':
    # 方式1：send 方法不传参，使用对象自己的属性
    buyer_login_api = BuyerLoginApi(username="hongyao", password="e10adc3949ba59abbe56e057f20f883e")
    resp = buyer_login_api.send().json()
    print(resp)
    # 方式2：send 方法传参，不传的参数使用默认属性
    # resp = buyer_login_api.send(data={'username': 'shamo', 'password':
    #     'sdhjhjashashdh', 'captcha': '1512', 'uuid': 'sahhsahshshshsh'})
    print(resp.json())
    
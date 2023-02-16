"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/15
    Time: 11:26
"""
from request_study.pinter_session import case_login


class TestLogin:
    # 在类中是以方法作为用例的

    # 密码为空
    def test_username_is_null(self):
        resp = case_login(password='')
        '''针对对象响应中的数据做断言'''
        # 断言状态码为200
        assert resp.status_code == 200
        # 断言响应信息中的 code 为 '1'
        resp = resp.json()
        assert resp['code'] == "1"
        # 断言 message 参数为空
        assert resp['message'] == '参数为空'



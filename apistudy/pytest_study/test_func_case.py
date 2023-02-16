"""
    Created with PyCharm.
    Description:
        以 pinter_session 中 login 函数为测试目标
    User: hong yaO
    Date: 2023-02-2023/2/15
    Time: 11:12
"""

# 1.用户名为空
from request_study.pinter_session import case_login


def test_username_is_null():
    resp = case_login(username='')
    '''针对对象响应中的数据做断言'''
    # 断言状态码为200
    assert resp.status_code == 200
    # 断言响应信息中的 code 为 '1'
    resp = resp.json()
    assert resp['code'] == "1"
    # 断言 message 参数为空
    assert resp['message'] == '参数为空'


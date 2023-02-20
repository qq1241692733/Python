"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/18
    Time: 20:49
"""
from typing import List

import pytest

from api.baseapi import BaseBuyerApi
from api.buyer.cart_apis import BuyNowApi
from api.buyer.login_apis import BuyerLoginApi
from db_study.db_util import DBUtil
from redis_study.redis_connect import RedisUtil
from sdk.shop_apis import buyer_login


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item 表示每个测试用例， 解决用例中文名称显示的问题
    for item in items:
        # item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")

@pytest.fixture(scope='session', autouse=True)
def get_buyer_token():
    buyer_login_api = BuyerLoginApi(username="hongyao", password="e10adc3949ba59abbe56e057f20f883e")
    resp = buyer_login_api.send().json()
    print(resp)
    BaseBuyerApi.buyer_token = resp['access_token']
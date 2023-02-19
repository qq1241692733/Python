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
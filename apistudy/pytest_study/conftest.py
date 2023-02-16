"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/16
    Time: 18:58
"""

# pytest 测试执行时谁会自动扫描，在这里重写pytest钩子函数
from typing import List

import pytest

from sdk.shop_apis import buyer_login


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item 表示每个测试用例， 解决用例中文名称显示的问题
    for item in items:
        # item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")

# 为了统一管理，将fixture放在这里写
# 在整个测试开始前，解决登录问题

# 自定义 fixture 完成登录
@pytest.fixture(scope='session', autouse=True)
def buyer_token():
    buyer_login()
    print()
    print("这个是 conftest 中的买家登录")
    yield  # 后置处理
    print("买家退出登录")
'''
scope 作用域：
    session:表示一次pytest的执行，这个fixture只会执行一次，不管被调用多少次
    package: 表示一个包下只会被执行一次，多个包执行多次
    module: 一个模块只会被执行一次
    class：一个类下
    function: 默认级别，一个方法
autouse 自动执行：
    默认 False
    
yield 关键字
    1.返回数据
    2.区分后置操作
'''

@pytest.fixture(scope='class', autouse=False)
def creat_goods():
    print("创建一个商品")
    yield '商品id:1'
    print('清除商品数据')

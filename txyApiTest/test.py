"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/18
    Time: 20:56
"""

def fun(**kwargs):
    print(type(kwargs), kwargs)
    dict1 = {**kwargs}
    print(dict1)
    fun2(**kwargs)

def fun2(url, meathon, data=None, headers=None):
    print(data)
    print(headers)


if __name__ == '__main__':
    fun(url=None, meathon=None)
    fun(url='http666', meathon='post', data={'a': 1, 'b': 2}, headers='jhy')



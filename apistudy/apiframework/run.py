"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/18
    Time: 20:49
"""
import os
import pytest
if __name__ == '__main__':
    # 这行表示执行pytest测试，会自动扫描pytest.ini中的参数
    pytest.main()
    # 增加一个allure命令行的动作，生成临时测试报告
    os.system('allure serve report/data')
    # 如果你想生成html数据，然后在手动打开
    os.system('allure generate report/data -o report/html --clean')

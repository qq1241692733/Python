"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-02-2023/2/20
    Time: 21:11
"""
import pandas

from get_project_path import project_path


def read_excel(file_path, sheet_name):
    # keep_default_na:单元格为空，是否n使用NA代替,False 为空字符串
    res = pandas.read_excel(f'{project_path}{file_path}', sheet_name=sheet_name, keep_default_na=False, engine='openpyxl')
    print(f'{project_path}{file_path}')
    print(res, type(res))
    # res 不符合pytest参数化数据格式，转换为二维数组
    row = res.shape[0]  # 获取总行数
    col = res.shape[1]  # 总列数
    data = []
    for l in range(row):
        line = []
        for c in range(col):
            cell_data = res.iloc[l, c]
            line.append(cell_data)
        data.append(line)
    return data



if __name__ == '__main__':
    print(read_excel('/data/mtxshop_testdata.xlsx', '立即购买接口测试数据'))

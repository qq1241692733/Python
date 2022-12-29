import random

number = 1
print('number：%d'%(number))
print("number：{}".format(number))
print(f'number:{number}')

data_list = ['3', '4', '1', '3', '5']
"""
控制台模拟随机数抽奖，遇到 quit 退出
"""
msg = ''
while msg != 'quit':
    in_name = input()
    name = random.choice(data_list)
    print(f'恭喜{name}获奖')
    data_list.remove(name)


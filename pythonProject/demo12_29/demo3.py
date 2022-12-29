import random

"""
抽奖  1-300号员工
30等奖30名
2等奖10名
1等奖1名
"""
# brother = []
# for i in range(1, 301):
#     brother.append(i)
# 
# brother = list(range(1, 301))

# 推导式
brother = [i for i in range(1, 301)]
print(brother)
print("--"*20)
third = random.sample(brother, 10)
print(third)

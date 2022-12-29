import random

num = "20"
print(num)

print("********************")
print(bool(0))
array = [1, 2, 3]
print(array)
print("**" * 20)
print(bool("你好"))

print("**" * 20)
number = int(random.randrange(1, 100))
print(type(number))
print(number)
while True:
    try:
        my_number = input("请输入数字:")
        if int(my_number) > number:
            print("猜大了")
        elif int(my_number) < number:
            print("猜小了")
        else:
            print("猜对了")
            break
    except:
        print("输入格式不对")
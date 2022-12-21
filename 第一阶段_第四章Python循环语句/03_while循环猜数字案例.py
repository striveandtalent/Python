"""
演示while循环的基础案例-猜数字
"""

import random

# num = random.randint(1, 100)
# # Todo:random的知识点：random(a,b)-->生成一个[a,b]之间的整数
# user = int(input("请输入你猜的数字"))
# count = 1
# if (user == num):
#     print("恭喜你，猜对了！")
# else:
#     while user != num:
#         if (user > num):
#             print("你猜的数字过大")
#             count += 1
#             user = int(input("请再猜："))
#             continue
#         else:
#             print("你猜的数字过小")
#             count += 1
#             user = int(input("请再猜："))
#             continue
#
# print(f"你一共猜了{count}次，终于猜对了")


num = random.randint(1, 100)
# Todo:random的知识点：Python中的random(a,b)-->生成一个[a,b]之间的整数
# 通过一个bool类型的变量，做循环是否继续的标记,如果猜中了，就把true改为false
flag = True
count = 0
while flag:
    guess_num = int(input("请输入你猜测的数字:"))
    count += 1
    if guess_num == num:
        print("猜中了")
        # 终止循环的条件
        flag = False
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")
print(f"你总共猜测了{count}次")

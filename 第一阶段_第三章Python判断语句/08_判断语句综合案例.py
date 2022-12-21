import random

num = random.randint(1, 10)
input_num = int(input("请输入你猜的数字"))
if input_num == num:
    print('恭喜你猜对了')
elif input_num > num:
    print("猜大了")
    input_num = int(input("请重新输入你猜的数字"))
    if input_num == num:
        print("猜对了")
    elif input_num > num:
        print("猜大了")
        input_num = int(input("请重新输入你猜的数字"))
        if input_num == num:
            print("猜对了")
        elif input_num > num:
            print("猜大了")
        else:
            print("猜小了")
    else:
        print("猜小了")
        input_num = int(input("请重新输入你猜的数字"))
        if input_num == num:
            print("猜对了")
        elif input_num > num:
            print("猜大了")
        else:
            print("猜小了")
else:
    print("猜小了")
    input_num = int(input("请重新输入你猜的数字"))
    if input_num == num:
        print("猜对了")
    elif input_num > num:
        print("猜大了")
        input_num = int(input("请重新输入你猜的数字"))
        if input_num == num:
            print("猜对了")
        elif input_num > num:
            print("猜大了")
        else:
            print("猜小了")
    else:
        print("猜小了")
        input_num = int(input("请重新输入你猜的数字"))
        if input_num == num:
            print("猜对了")
        elif input_num > num:
            print("猜大了")
        else:
            print("猜小了")

print('动物园')
if int(input('请输入身高')) >= 120:
    print('身高大于120，不可以免费')
    print('不过如果你的vip是3依然免费')
    if int(input("请输入你的vip等级(1~3)")) == 3:
        print('你的VIP等级是3，可以免费')
    else:
        print("你的等级不足，不可以免费")

else:
    print("身高低于120，可以免费")

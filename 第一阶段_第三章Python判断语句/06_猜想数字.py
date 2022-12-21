num = 5
# 通过键盘大的输入获取猜想的数字，通过多次if elif else 的组合进行猜想比较
if int(input('请猜想一个数字：')) == num:
    print("恭喜第一次就成功了")
elif int(input('猜错了，再猜一次')) == num:
    print('猜对了')
elif int(input('猜错了，再猜一次')) == num:
    print('恭喜最后一次机会你猜对了')
else:
    print("猜错了")

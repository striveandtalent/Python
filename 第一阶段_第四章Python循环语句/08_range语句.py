"""
语法1:range(num)
    获取一个从0开始，到num结束的数字序列，左闭右开(不含num本身)
语法2：range(num1,num2)
    获得一个从num1开始，到num2结束的数字序列(左闭右开)
语法3：range(num1,num2,step)
    同上，但是数字之间的步长，以step为准，默认为1
"""

for x in range(6):
    print(x)

for i in range(5, 10, 2):  # [5,7,9]，所以送3次
    print("送玫瑰花")

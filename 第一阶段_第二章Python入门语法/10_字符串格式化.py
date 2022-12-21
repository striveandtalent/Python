"""
通过占位的形式拼接字符串(字符串格式化)
%s:将内容转换成字符串，再放入占位位置
%d:将内容转换成整数，再放入占位位置
%f:将内容转换成浮点型，再放入占位位置
"""

# %表示：我要占位；s表示将变量变成字符串放入占位的地方
name = "黑马程序员"
message = "学IT就来%s", name
print(message)
# 输出:('学IT就来%s', '黑马程序员')


name2 = "黑马程序员"
message = "学IT就来%s" % name2
print(message)
# 输出:学IT就来黑马程序员


class_num = 57
avg_salary = 16781
print("Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary))

name3 = "传播智客"
set_up_year = 2006
stock_price = 19.99
message2 = "我是：%s，我成立于：%d，我今天的股价是：%f" % (name3, set_up_year, stock_price)
print(message2)

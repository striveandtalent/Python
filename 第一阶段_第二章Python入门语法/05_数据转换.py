"""
int(X):将X转换为一个整数
float(X):将X转换为一个浮点数
str(X):将X转换为字符串
和type()语句一样，这三个语句都是带返回值的，可以用print输出，或用变量存储
"""

# 将数字类型换成字符串
num_str = str(50)
print(type(num_str), num_str)
# print(type(str(50)))
# num_str_two = type(str(50))
# print(num_str_two)
float_str = str(13.14)
print(float_str, float_str)

# 将字符串转换成数字。
# 万物皆可转字符串，但想将字符串转数字那就一定要确保字符串内都是数字才可以
num = int("11")
print(type(num), num)

num2 = float("13.14")
print(type(num2), num2)

# 整数转浮点数
num3 = float(100)
print(type(num3), num3)

# 浮点数转整数
# 直接抹掉小数点后面的数
num4 = int(13.14)
print(type(num4), num4)

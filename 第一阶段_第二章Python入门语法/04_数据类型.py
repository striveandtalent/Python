"""
type():
不仅能够查看字面量的数据类型，还能够查看变量存储的数据类型
"""

# 使用print直接输出类型信息
print(type(50))
print(type(13.14))
print(type("hello"))

print("==========================================")
# 使用变量存储type()语句的结果
int_type = type(50)
float_type = type(13.14)
string_type = type("hello")
print(int_type)
print(float_type)
print(string_type)

print("==============================================")
# 查看变量中存储的数据类型
name = "hello"
print(type(name))

print("==============================================")
# name_type变量可以存储变量name的类型信息，是因为type()语句执行完会返回执行的结果
name = "world"
name_type = type(name)
print(name_type)

# Python中变量没有类型,平时‘字符串变量’指的是变量里面存储了字符串字面量

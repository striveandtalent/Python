"""
知识点 1：print("XXX")具有换行输出的特点
print("xxx",end='')取消换行的特点
"""
print("Hello")
print("World")

print("Hello", end='')
print("World")

"""
知识点 2：在字符串中,\t效果等同于在键盘上按下tab键，可以让多行字符串进行对齐
"""
print("Hello\tWorld")
print("itheima best")

# 案例：通过while循环打印九九乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i * j} \t", end='')

        j += 1
    i += 1

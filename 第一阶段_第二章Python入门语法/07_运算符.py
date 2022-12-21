"""
演示Python中的各类运算符
"""

# 算数运算符：+、-、*、/、//(取整数)、%(取余)、**(指数)
print("1+1=", 1 + 1)
print(type(1 + 1))

print("2-1=", 2 - 1)
print(type(2 - 1))

print("3*3=", 3 * 3)
print(type(3 * 3))

print("4/2=", 4 / 2)
print(type(4 / 2))

print("11//2=", 11 // 2)
print(type(11 // 2))

print("9%2=", 9 % 2)
print(type(9 % 2))

print("2**2=", 2 ** 2)
print(type(2 ** 2))
print("====================================")
#  赋值运算符：=
# 复合赋值运算符：+=、-=、*=、/=、%=、**=、//=
num = 1
num %= 2
print("1%=2 =", num)  # num %= 2  -->  num = num % 2

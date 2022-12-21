"""
演示Python的input语句获取键盘的输入信
input()接受的输入默认是str类型，如果有其他需要要进行类型转换
"""
# print("请告诉我你是谁?")
name = input("请告诉我你是谁?")
print(f"我知道了,你是{name}")

# 输入数字类型
password = input("请告诉我那你的银行卡密码:")
print(f"你输入的银行卡密码类型是{type(password)}")
password = int(password)
print(f"经过转换后你输入的银行卡密码类型是{type(password)}")

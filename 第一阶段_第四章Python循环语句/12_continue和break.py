"""
continue:中断本次循环，直接进入下一次循环
可用于for循环和while循环
"""

for i in range(1, 6):
    print("语句1")
    continue
    print("语句2")

for j in range(1, 6):
    print("语句1")
    for k in range(1, 6):
        print("语句2")
        continue
        print("语句3")
    print("语句4")

"""
break:直接结束循环
可用于for和while循环，效果一致
"""

for o in range(1, 6):
    print("语句1")
    break
    print("语句2")
print("语句3")

for y in range(1, 6):
    print("语句1")
    for e in range(1, 6):
        print("语句2")
        break
        print("语句3")
    print("语句4")

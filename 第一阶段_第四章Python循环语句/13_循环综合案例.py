"""
案例：发工资
        某公司，账户余额有1w元，给20名员工发工资。
        ·员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
        ·领工资时，财务判断员工的绩效分（1-10)（随机生成)，如果低于5，不发工资，换下一位
        ·如果工资发完了，结束发工资。
"""

money = 10000

for i in range(1, 21):

    # randint 是闭区间
    import random

    score = random.randint(1, 10)

    if score > 5:
        money -= 1000
        print(f"向员工{i}发放工资1000元,账户余额还剩余{money}")
        if money == 0:
            print("工资发完了，下个月领取吧")
            break
    else:
        print(f"员工{i},绩效分{score},低于5，不发工资，下一位")

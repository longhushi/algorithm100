"""
一辆卡车违反交通规则，撞人后逃跑。现场有三人目击该事件，但都没有记住车号，只记下了车号的一些特征。甲说：牌照的前两位数字是相同的；乙说：牌照的后两位数字是相同的，
但与前两位不同；丙是数学家，他说，4位的车号刚好是一个整数的平方。请根据以上线索求出车号。
"""
import math

for a in range(0,10):
    for b in range(0,10):
        num = 1000*a + 100*a + 10*b + b
        if b==a:
            continue
        elif math.sqrt(num)==int(math.sqrt(num)):
            print(num)
# 24点游戏
"""
在屏幕上输入1～10范围内的4个整数（可以有重复），对它们进行加、减、乘、除四则运算后（可以任意的加括号限定计算的优先级），寻找计算结果等于24的表达式。
"""
# 遍历三级运算，加减乘除都可能。1代表加，2代表减，3代表乘，4代表除，遍历所有五种优先级情况

def solve(num1,num2,num3,num4):
    op = ["#","+","-","*","/"]
    flag = False
    for op1 in range(1,5):
        for op2 in range(1,5):
            for op3 in range(1,5):
                if calc_model1(num1,num2,num3,num4,op1,op2,op3)==24:
                    print("(({} {} {}) {} {}) {} {}".format(num1,op[op1],num2,op[op2],num3,op[op3],num4))
                    flag = True
                if calc_model2(num1,num2,num3,num4,op1,op2,op3)==24:
                    print("({} {} ({} {} {})) {} {}".format(num1,op[op1],num2,op[op2],num3,op[op3],num4))
                    flag = True
                if calc_model3(num1,num2,num3,num4,op1,op2,op3)==24:
                    print("{} {} ({} {} ({} {} {}))".format(num1,op[op1],num2,op[op2],num3,op[op3],num4))
                    flag = True
                if calc_model4(num1,num2,num3,num4,op1,op2,op3)==24:
                    print("{} {} (({} {} {}) {} {})".format(num1,op[op1],num2,op[op2],num3,op[op3],num4))
                    flag = True
                if calc_model5(num1,num2,num3,num4,op1,op2,op3)==24:
                    print("({} {} {}) {} ({} {} {})".format(num1,op[op1],num2,op[op2],num3,op[op3],num4))
                    flag = True
    if flag==False:
        print("对不起，你所输入的四个数字无法得到24")
                

def calc(op, x, y):
    if op==1:
        return x+y
    elif op==2:
        return x-y
    elif op==3:
        return x*y
    elif op==4:
        return x/y

# ((A B) C) D
def calc_model1(num1,num2,num3,num4,op1,op2,op3):
    r1 = calc(op1,num1,num2)
    r2 = calc(op2,r1,num3)
    r3 = calc(op3,r2,num4)
    return r3

# (A (B C)) D
def calc_model2(num1,num2,num3,num4,op1,op2,op3):
    r1 = calc(op2,num2,num3)
    r2 = calc(op1,num1,r1)
    r3 = calc(op3,r2,num4)
    return r3

# A (B (C D))
def calc_model3(num1,num2,num3,num4,op1,op2,op3):
    r1 = calc(op3,num3,num4)
    r2 = calc(op2,num2,r1)
    r3 = calc(op1,num1,r2)
    return r3

# A ((B C) D)
def calc_model4(num1,num2,num3,num4,op1,op2,op3):
    r1 = calc(op2,num2,num3)
    r2 = calc(op3,r1,num4)
    r3 = calc(op1,num1,r2)
    return r3

# (A B) (C D)
def calc_model5(num1,num2,num3,num4,op1,op2,op3):
    r1 = calc(op1,num1,num2)
    r2 = calc(op3,num3,num4)
    r3 = calc(op2,r1,r2)
    return r3

if __name__ == "__main__":
    s = input("请输入四个1~10范围内的整数，以逗号分隔:")
    arr = s.split(",")
    num1 = int(arr[0])
    num2 = int(arr[1])
    num3 = int(arr[2])
    num4 = int(arr[3])
    solve(num1,num2,num3,num4)
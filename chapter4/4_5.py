# 最小公倍数
"""
求任意两个正整数的最小公倍数（Least Common Multiple，LCM）。
"""
# 先得到两个数之间的最小值，然后从它的2倍开始，如果可以整除另一个数就是最小公倍数

def get_smaller(a,b):
    if a < b:
        return a
    else:
        return b
    
def get_bigger(a,b):
    if a < b:
        return b
    else:
        return a
    
def get_num(a,b):
    a = get_smaller(a,b)
    b = get_bigger(a,b)
    num = a
    i = 1
    while num%b!=0:
        num = a*i
        i += 1
    return num

if __name__ == "__main__":
    print("请输入两个正整数：")
    a = input()
    b = input()
    a = int(a)
    b = int(b)
    print("{}和{}的最小公倍数是：{}".format(a,b,get_num(a,b)))
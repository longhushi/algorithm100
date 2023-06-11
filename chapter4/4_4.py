# 最大公约数
"""
参考4_2题的解法
"""
# 定义一个函数求两个数的最大公约数，如果最大公约数为1，说明是最简分数了。
def get_num(a,b):
    m = 1
    for i in range(1,a+1): # 从1遍历到a
        if a%i == 0 and b%i==0:
            if i>=m:
                m = i
    return m

if __name__ == "__main__":
    print("请输入两个正整数：")
    a = input()
    b = input()
    a = int(a)
    b = int(b)
    print("{}和{}的最大公约数是：{}".format(a,b,get_num(a,b)))
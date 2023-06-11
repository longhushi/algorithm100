# 列出真分数序列
"""
按递增顺序依次列出所有分母为40、分子小于40的最简分数。
"""
# 定义一个函数求两个数的最大公约数，如果最大公约数为1，说明是最简分数了。
def get_num(a,b):
    m = 1
    for i in range(1,a+1): # 从1遍历到a
        if a%i == 0 and b%i==0:
            if i>=m:
                m = i
    return m

def solve():
    for i in range(1,40):
        if get_num(i, 40)==1:
            print("%d/%d"%(i,40))

if __name__ == '__main__':
    print('分母为40、分子小于40的最简分数为：')
    solve()
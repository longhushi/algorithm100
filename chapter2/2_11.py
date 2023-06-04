# 换分币
"""
将5元的人民币兑换成1元、5角和1角的硬币，共有多少种不同的兑换方法。
"""
# 其实这个题目和之前的类似，设1元有i个，5角有j个，1角有k个，10*i+5*j+1*k=50
def solve():
    for i in range(0,6):
        for j in range(0,11):
            for k in range(0, 51):
                if (10*i+5*j+1*k)==50:
                    print('可以兑换为：{}个1元，{}个5角，{}个1角'.format(i,j,k))

if __name__ == '__main__':
    solve()
# 最佳存款方案
"""
假设银行一年整存零取的月息为0.63%。现在某人手中有一笔钱，他打算在今后5年中的每年年底取出1000元。到第五年时刚好取完，请算出他存钱时应存入多少。
"""
# 假设初始为钱为m，每年年底为m(1+12*0.63%)，减去1000后，剩下的钱第二年继续享受利息，到第五年正好剩下1000，取完。
def solve():
    m = 0 # 因为第五年钱取完了，所以开始m=0，倒着反推初始的钱数
    for i in range(5):
        #m = m(1+12*0.0063)-1000
        m = (m+1000)/(1+12*0.0063)
    return m

if __name__ == '__main__':
    m = solve()
    m = round(m,2)
    print('用户存钱时应该存入：{}元'.format(m))
    
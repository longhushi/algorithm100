# 多项式之和
"""
计算下列多项式的值
"""
# 用循环解决，分子为1，分母为阶乘
def solve():
    sum = 0 
    for i in range(1,51):
        n = 1
        for j in range(1,i+1):
            n = n*j
        sum += 1/n
    return sum

if __name__ == "__main__":
    r = solve()
    print("多项式的值是：{}".format(r))
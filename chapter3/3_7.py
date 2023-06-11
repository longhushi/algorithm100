# 高次方数的尾数
"""
求13的13次方的最后三位数
"""
# 不用真的取乘，由于最后三位数只有被乘数的最后三位决定，所以可以只管后三位即可。

def solve():
    a = 13
    for i in range(1,13):
        a = a*13
        a = str(a)[-3:]
        a = int(a)
    return a

print(str(169)[-3:])

if __name__ == '__main__':
    a = solve()
    print("13的13次方的最后三位数是：{}".format(a))
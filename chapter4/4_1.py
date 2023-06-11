# 将真分数分解为埃及分数
"""
现输入一个真分数，请将该分数分解为埃及分数。
真分数（a proper fraction）是指分子比分母小的分数，其分数值小于1。如1/2、3/5、8/9等都是真分数。
所谓埃及分数是指分子位1的分数。
"""
# 如果分母可以整除分子就整除，如果不可以整除了，就分出一个1/分母，然后继续分母除分子，如果不可以整除就继续分出1，直到分子变成1
def decompose(f,m):
    # 分子f,分母m
    li = []
    if f>1:
        if m%f==0:
            m = m//f
            li = li + [(1,m)]
        else:
            li = li + [(1,m)]
            li = li + decompose(f-1,m)
    else:
        li = li + [(1,m)]
    return li    

if __name__ == '__main__':
    li = decompose(3,5)
    print(li)
    print('3/5 分解为埃及分数结果为：')
    for (f,m) in li:
        print('%d/%d'%(f,m))

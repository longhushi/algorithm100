# 分数比较
"""
比较两个分数的大小
"""
# 把两个分数的分母变成一样，然后直接比较分子即可
def compare(f1, m1, f2, m2):
    if m1 != m2: # 如果分母不同，则统一分母，修改分子
        m = m1*m2
        f1 = f1*m2
        f2 = f2*m1
    if f1 == f2:
        return 0
    elif f1 < f2:
        return -1
    else:
        return 1
    
if __name__ == "__main__":
    print("请输入两个分数：")
    f1 = input("第一个数的分子：")
    m1 = input("第一个数的分母：")
    f2 = input("第二个数的分子：")
    m2 = input("第二个数的分母：")
    f1 = int(f1)
    m1 = int(m1)
    f2 = int(f2)
    m2 = int(m2)
    r = compare(f1,m1,f2,m2)
    if r==0:
        print("两个分数相等")
    elif r==-1:
        print("{}/{}大于{}/{}".format(f2,m2,f1,m1))
    else:
        print("{}/{}大于{}/{}".format(f1,m1,f2,m2))

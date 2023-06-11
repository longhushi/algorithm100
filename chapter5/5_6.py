# 孪生素数
"""
所谓孪生素数指的是间隔为2的两个相邻素数，因为它们之间的距离已经近得不能再近了，如同孪生兄弟一样，故将这一对素数称为孪生素数。
编程求出3～1000以内的所有孪生素数。
"""
# 首先获取3~1000内所有素数列表，然后遍历素数，查询该素数+2是否也在列表中，若是则是孪生素数，否则就不是。
# 复用上一题的函数
def is_su(num):
    if num==2 or num==1:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True
                 
def get_su(start, end):
    su_list = []
    for i in range(start,end+1):
        if is_su(i):
            su_list.append(i)
    return su_list

if __name__ == '__main__':
    su_list = get_su(3,1000)
    twins = []
    for su in su_list:
        if su+2 in su_list:
            twins.append((su,su+2))
    print("3~1000以内的所有孪生素数：",twins)
    print("共有{}对".format(len(twins)))
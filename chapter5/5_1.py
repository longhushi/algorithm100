# 素数
"""
求给定范围start～end之间的所有素数。
"""
# 素数是除了1和自身之外没有其它因子的数

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
    su_list = get_su(1,1000)
    print("1和1000之间的素数共有{}个，分别是：{}".format(len(su_list),su_list))
                
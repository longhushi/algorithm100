# 梅森素数
"""
梅森数（Mersenne Prime）指的是形如2^n-1的正整数，其中指数n是素数，记为Mn。
如果一个梅森数是素数，则称其为梅森素数。例如22-1＝3、23-1＝7都是梅森素数。
试求出指数n<20的所有梅森素数。
"""
# 先得到20以内的素数列表，然后求2^n-1的值，判断其是否为素数
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
    su_list = get_su(1,20)
    result_list = []
    for su in su_list:
        if is_su(2**su-1):
            result_list.append(2**su-1)
    print("n<20的所有梅森素数：",result_list)

# 哥德巴赫猜想
"""
2000以内的不小于4的正偶数都能够分解为两个素数之和（即验证歌德巴赫猜想对2000以内的正偶数成立）。
"""
# 先列出2000以内的素数，再求和，如果和等于正偶数就是对的。

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

import time 

# 遍历正偶数，遍历所有素数列表，如果可以由两个素数的和组成，则猜想成立
def prove():
    time1 = time.time()
    su_list = get_su(1,2000)
    for i in range(4,2000):
        if i%2==0: # 正偶数
            flag = False
            for j in su_list:
                for k in su_list:
                    if j!=k and j+k == i:
                        flag = True
            if flag == False:
                return False  
    time2 = time.time()
    print("时间共花了{}".format(time2-time1))
    return True

# 另一种更高效的解法：遍历所有正偶数，再遍历所有素数，如正偶数-素数的差也是素数，则猜想成立，这样可以减少一次循环
def guess():
    time1 = time.time()
    su_list = get_su(1,2000)
    for i in range(4,2000):
        if i%2==0: # 正偶数
            flag = False
            for j in su_list:
                if is_su(i-j):
                    flag = True
        if flag == False:
            return False
    time2 = time.time()
    print("时间共花了{}".format(time2-time1))
    return True

if __name__ == '__main__':
    print("哥德巴赫猜想对2000以内的正偶数成立是：{}".format(prove())) #  时间共花了3.9954566955566406
    print("哥德巴赫猜想对2000以内的正偶数成立是：{}".format(guess())) #  时间共花了1.2402830123901367
    # 可见第二种方法快了三倍以上

    
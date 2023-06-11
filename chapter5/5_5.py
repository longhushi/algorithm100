# 回文素数
"""
所谓回文素数指的是，对一个整数n从左向右和从右向左读其数值都相同且n为素数，则称整数n为回文素数。
对于偶数位的整数，除了11以外，都不存在回文素数。即所有的4位整数、6位整数、8位整数等都不存在回文素数。
求出所有不超过1000的回文素数。
"""
# 首先列出所有不超过1000的素数，然后直接判断三位素数就行，因为两位的只有11，然后在三位数里面判断是否是回文数

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

# 判断是否是回文数
def is_huiwen(num):
    num = str(num)
    arr = list(num)
    for i in range(len(arr)//2):
        if arr[i]!=arr[len(arr)-i-1]:
            return False
    return True

if __name__ == '__main__':
    su_list = get_su(100,1000)
    result_list = [11]
    for su in su_list:
        if is_huiwen(su):
            result_list.append(su)
    print("不超过1000的回文素数：{}".format(result_list))
# 可逆素数
"""
请从小到大输出所有4位数的可逆素数。可逆素数是指一个素数将其各位数字的顺序倒过来构成的反序数也是素数。
"""
# 获取所有的素数，并判断该数反过来是否是素数

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

def get_reverse(num):
    num = str(num)
    arr = list(num)
    arr.reverse()
    num2 = "".join(arr)
    return int(num2)

if __name__ == '__main__':
    su_list = get_su(1000,9999)
    result_list = []
    for su in su_list:
        reverse = get_reverse(su)
        if is_su(reverse):
            result_list.append(su)
    print("4位可逆素数共{}个，分别为：{}".format(len(result_list),result_list))

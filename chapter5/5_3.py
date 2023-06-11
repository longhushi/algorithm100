# 要发就发
"""
“1898——要发就发”。请将不超过1993的所有素数从小到大排成第一行，第二行上的每个数都等于它上面相邻两个素数之差。
编程求出：第二行数中是否存在若干个连续的整数，它们的和恰好为1898？假如存在的话，又有几种这样的情况？
"""
# 两个列表，一个是不超1993的素数，一个是相邻两个素数的差，然后遍历第二个列表，查找1898-i，是否也在该列表中。

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

def get_diff(li):
    r = []
    for i in range(len(li)-1):
        r.append(li[i+1]-li[i])
    return r

if __name__ == '__main__':
    su_list = get_su(2, 1993)
    diff_list = get_diff(su_list)
    print(su_list)
    print(diff_list)
    result_list = []
    
    for i in range(len(diff_list)):
        sum = 0
        for j in range(i, len(diff_list)):
            sum += diff_list[j]
            if sum == 1898:
                result_list.append((su_list[i],su_list[j+1]))
                continue
    print("一共有{}中情况，分别如下：{}".format(len(result_list), result_list))

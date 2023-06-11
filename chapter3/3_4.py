# 完数
"""
求某一范围内完数的个数。如果一个数等于它的因子之和，则称该数为“完数”（或“完全数”）。
例如，6的因子为1、2、3，而6=1+2+3，因此6是“完数”。
"""
# 循环遍历，获取到所有的因子，并且得到和，判断数字本身是否等于因子之和。

def is_perfect(num):
    factor_list = [] # 因子列表，存放一个数的因子
    for i in range(1,num):
        if num%i==0:
            factor_list.append(i) # 获取因子
    sum = 0
    for f in factor_list: # 遍历因子，对所有因子求和
        sum += f
    if sum==num: # 如果因子的和等于数字本身，则这个数字就是一个完数
        return True
    else:
        return False
    
print(is_perfect(6))

if __name__ == '__main__':
    for i in range(1,1000):
        if is_perfect(i):
            print("{} 是一个完数".format(i))    
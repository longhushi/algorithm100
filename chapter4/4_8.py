# 计算分数的精确值
"""
使用数组精确计算M/N（0<M<N≤100）的值。假如M/N是无限循环小数，则计算并输出它的第一循环节，同时要求输出循环节的起止位置（小数位的序号）。
"""
# 方法和书中介绍的一样，用数组保存数字，余数乘以10，再计算商的下一位
def solve(M,N):
    result = [] # 商列表
    last_list = [] # 余数列表
    result.append(0)
    last = M%N
    for i in range(1,100): # 最多计算100次
        if not last in last_list: # 只要现在的余数出现在之前的余数列表中，说明开始无限循环了，而当前的位置就是无限循环的开始位置
            last_list.append(last)
            last = last*10
            result.append(last//N)
            last = last%N
            
            if last==0:
                print("是有限不循环小数")
                return result
            elif i==99: # 如果一直除不尽，但是又没有发生循环，就认为是无限不循环小数
                print("是无限不循环小数")
        else:
            print("是无限循环小数")
            print("从第{}个位置开始无限循环".format(i-1))
            return result
        
if __name__ == '__main__':
    result = solve(25,95)
    print("25/95的精确结果是：0.",end='')
    for i in range(1,len(result)):
        print("%d"%result[i],end='')
        
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @desc: 计算分数精确值

if __name__ == "__main__":
    remainder = [0]*101                             # remainder存放除法的余数
    quotient = [0]*101                              # quotient 依次存放商的每一位
    print("请输入分子与分母大于0，小于等于100的分数")
    m = int(input("分子m = "))                        # 分子
    n = int(input("分母n = "))                        # 分母
    print("输入的分数为：%d/%d" %(m, n))
    print("%d/%d 的准确值是：0." %(m, n), end="")
    for i in range(1, 101):                         # i商的位数
        remainder[m] = i    # m：得到的余数；remainder[m]：该余数对应的商的位数
        m *= 10                                                     # 余数扩大10倍
        quotient[i] = m // n                        # 商
        m = m % n                                                   # 求余数
        if m == 0:                                                  # 余数为0则表示是有限小数
            j = 1
            while j <= i:
                print("%d" %quotient[j], end="")            # 输出商
                j += 1
            break                                                                   # 退出循环

        if remainder[m] != 0:                       # 若该余数对应的位在前面已经出现过
            j = 1
            while j <= i:
                print("%d" %quotient[j], end="")    # 输出循环小数
                j += 1
            print("\n分数的第一个循环节：%d" %remainder[m])
            print("循环节的起始位置为：%d" %i)
            break
        
            
            '''
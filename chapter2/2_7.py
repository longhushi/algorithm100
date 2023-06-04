# 爱因斯坦的数学题
"""
爱因斯坦出了一道这样的数学题：有一条长阶梯，若每步跨2阶，则最后剩一阶，若每步跨3阶，则最后剩2阶，若每步跨5阶，则最后剩4阶，若每步跨6阶，则最后剩5阶。
只有每次跨7阶，最后才正好一阶不剩。请问在1到n内，有多少个数能满足？
"""
# 取模运算

def solve(n):
    li = []
    for i in range(1,n):
        if i%2==1 and i%3==2 and i%5==4 and i%6==5 and i%7==0:
            print(i,"可以满足条件")
            li.append(i)
    return li

if __name__ == '__main__':
    li = solve(1000)
    print('一共有{}个数能满足'.format(len(li)))
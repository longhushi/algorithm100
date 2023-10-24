# pi的近似值
"""
蒙特卡罗方法的思路是，在一个单位边长的正方形中，以边长为半径，以一个顶点为圆心，在这个正方形上作四分之一圆。
在正方形中随机地投入很多点，使所投入的点落在正方形中每一个位置的机会相等。若点落入四分之一圆内则计数。
重复地向正方形中投入足够多的点，用落入四分之一圆内的点数除以总的点数，得到的就是π的四分之一的近似值。
"""
# x,y生成（0，1）之间的随机数，如果x**2+y**2开根号小于等于1,则表示落入圆中，计数
import random
import math

def solve():
    count1 = 0
    count2 = 0
    
    for i in range(10000000):
        x = random.random()
        y = random.random()
        if math.sqrt(x**2+y**2)<=1.0:
            count2 += 1
        count1 += 1
    pi = (count2/count1)*4
    return pi

if __name__ == '__main__':
    pi = solve()
    print('pi is: %f' % pi)
# 四方定理
"""
四方定理是数论中的重要定理，它可以叙述为“所有的自然数至多用4个数的平方和就可以表示出来”。编程验证
"""
# 四重循环i,j,k,t，i从0到数字的根号，j从0到i，k从0到j，t从0到k
import math

def solve(num):
    for i in range(0,int(math.sqrt(num))+1):
        for j in range(0,i):
            for k in range(0,j):
                for t in range(0,k):
                    r = i**2+j**2+k**2+t**2
                    if r==num:
                        print("success, prove it")
                        print("%d**2 + %d**2 + %d**2 + %d**2 = %d" % (i,j,k,t,num))
                        return
    

if __name__ == '__main__':
    num = input('Please enter a number:')
    num = int(num)
    solve(num)
# 勾股数
"""
求100以内的所有勾股数。所谓勾股数，是指能够构成直角三角形三条边的三个正整数（a，b，c）。
"""
# 循环即可
import math

# 这种方法最直观，但是会有重复
def solve(num=100):
    for i in range(1,num):
        for j in range(1,num):
            for k in range(1,num):
                if i**2 == j**2+k**2:
                    print("勾股数: {},{},{}".format(i,j,k))


# 这是书上的解法，更快也更好，两重循环就可以了
def solve2(num=100):
    for i in range(1,num):
        for j in range(i+1,num):
            c = int(math.sqrt(i**2+j**2)) # 平方根取整后，如果平方等于另两数的平方和就说明是勾股数
            if c**2 == i**2+j**2 and c<num:
                print("勾股数: {},{},{}".format(i,j,c))

if __name__ == "__main__":
    solve2()

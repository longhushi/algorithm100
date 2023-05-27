# 牛顿迭代法求方程根
"""
编写用牛顿迭代法求方程根的函数。方程为ax^3+bx^2+cx+d=0,系数a,b,c,d由主函数输入，求x在1附件的一个实根。求出根后，由主函数输出。
"""
# 牛顿迭代法：x = x0 - f(x0)/df(x0),迭代到abc(x-x0)<=10e-5
def solve(a,b,c,d):
    x = 1.5
    f = a*x**3+b*x**2+c*x+d
    df = 3*a*x**2 + 2*b*x + c
    x_new = x - f/df
    while abs(x_new - x)>10e-5:
        x = x_new
        f = a*x**3+b*x**2+c*x+d
        df = 3*a*x**2 + 2*b*x + c
        x_new = x - f/df
    return x_new

if __name__ == '__main__':
    a = 2
    b = -4
    c = 3
    d = -6
    print(a**3)
    print('the result is: {}'.format(solve(a,b,c,d)))

    
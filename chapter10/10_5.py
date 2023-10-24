# 角谷猜想
"""
角谷猜想的内容是任给一个自然数，若为偶数则除以2，若为奇数则乘以3再加1，
这样得到一个新的自然数之后再按照前面的法则继续演算，若干次以后得到的结果必然为1。
在数学文献里，角谷猜想也常常被称为“3X+1问题”。请编程验证角谷猜想。
"""
# 定义一个循环，反复执行该计算，直到得到1
def solve(num):
    while num!=1:
        if num%2==0: # 如果是偶数
            num = num/2
        else:
            num = num*3+1
    print('prove it! The result is 1')

if __name__ == '__main__':
    num = input('Please enter a number:')
    num = int(num)
    solve(num)
# 亲密数
"""
如果整数A的全部因子（包括1，不包括A本身）之和等于B，且整数B的全部因子（包括1，不包括B本身）之和等于A，则将整数A和B称为亲密数。
求3000以内的全部亲密数。
"""
# 求一个数字对，获得一个数字的全部因子，求和，和等于另一个数字。
def is_close(num1,num2):
    if num1 == num2: # 数字本身不是亲密数
        return False 
    sum1 = 0
    sum2 = 0
    for i in range(1,num1):
        if num1%i==0: # 获取因子
            sum1 += i
    for i in range(1,num2):
        if num2%i==0:
            sum2 += i

    if sum1==num2 and sum2==num1:
        return True
    else:
        return False
    
# 我上面的解法效率太低了，可以考虑书上的解法，既然A的因子和等于B，那可以把第一个数A的因子和求出来当B，再求B的因子和看看是否等于A即可。这样只要循环一次3000个数，不需要两次循环。
def get_close():
    for a in range(3000):
        b = 0
        sum = 0
        for j in range(1,a): # 获取a的因子和
            if a%j==0:
                b += j
        for k in range(1,b): # 获取b的因子和
            if b%k==0:
                sum += k
        if sum==a and a<b: # 因为如果a==b那就是自己本身，没有意义，如果a<b，那其实和a>b的时候是一样的，只是a,b调换了一下而已。
            print("{}和{}是一对亲密数".format(a,b))
        
        
    
if __name__ == '__main__':
    # for i in range(3000):
    #     for j in range(i,3000):
    #         if is_close(i,j):
    #             print("{} 和 {} 是一对亲密数".format(i,j))
    get_close()

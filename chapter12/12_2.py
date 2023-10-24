# 数据加密
"""
某个公司采用公用电话来传递数据，传递的数据是4位的整数，且要求在传递过程中数据是加密的。
数据加密的规则为：将每位传递的数字都加上5，之后用和除以10的余数来代替该数字，最后将第一位和第四位数字交换，第二位和第三位数字交换。
"""
# 按要求进行加密
def jiami(num):
    li = list(num)
    r = []
    for n in li:
        n = int(n)
        n = n+5
        n = n%10
        r.append(str(n))
    return r[3]+r[2]+r[1]+r[0]

if __name__ == '__main__':
    num = input('Please enter a number:')
    result = jiami(num)
    print(result)
    
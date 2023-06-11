# 自守数
"""
自守数是指一个数的平方的尾数等于该数自身的自然数。例如，5的平方=25，25的平方=625，76的平方=5776，9376的平方=87 909 376。求100 000以内的自守数。
"""
# 求一个数的平方，获取该数的位数，从平方数尾部截取相应的位数，转成数字，若相等则返回
def is_zishou(num):
    square = num**2
    num = str(num)
    square = str(square)
    arr1 = list(num)
    arr2 = list(square)
    sub = arr2[-len(arr1):] # 获取尾部的数字，长度和原数字相同
    num2 = ''
    for i in sub:
        num2+=str(i)
    #print(num2)
    if int(num) == int(num2):
        return True
    else:
        return False
    
print(is_zishou(5))

if __name__ == '__main__':
    for i in range(10, 100000):
        if is_zishou(i):
            print("{} 是一个自守数".format(i))
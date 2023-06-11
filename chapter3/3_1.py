# 回文数
"""
打印所有不超过n（取n<256）的其平方具有对称性质的数（也称回文数）。
"""
# 判断一个数的平方，他的第一位是否和最后一位相同，第二位是否和倒数第二位相同，以此类推

def is_huiwen(num):
    num = str(num)
    arr = list(num)
    for i in range(len(arr)//2):
        if arr[i]!=arr[len(arr)-i-1]:
            return False
    return True

#print(is_huiwen(12*12))

if __name__ == '__main__':
    for i in range(256):
        if is_huiwen(i**2):
            print("{} 的平方 {} 是回文数".format(i, i**2))
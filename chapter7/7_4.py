# 人机猜数
"""
由计算机随机产生一个4位整数，请人猜这4位整数是多少。
人输入一个4位数后，计算机首先判断其中有几位猜对了，并且对的数字中有几位位置也正确，
将结果显示出来，给人以提示，请人再猜，直到人猜出计算机随机产生的4位数是多少为止。
"""
# 先提示有几个数字正确，再提示有几个位置也正确
import random

if __name__ == '__main__':
    num = random.randint(1000,9999)
    num = str(num)
    arr1 = list(num)
    f = open('1.txt', 'w')
    f.write(num + '\n')
    f.close()

    while(True):
        guess = input('请输入你猜的四位数：')
        arr2 = list(guess)
        r1 = 0
        r2 = 0
        for c in list(set(arr1)):
            if c in arr2:
                r1 += 1
        for i in range(4):
            #if arr2[i] in arr1:
            #    r1 += 1
            if arr2[i] == arr1[i]:
                r2 += 1
        print("有{}个数字猜对了，有{}个数字位置也对了".format(r1,r2))
        if r2==4:
            print('恭喜，猜中了！')
            break
    
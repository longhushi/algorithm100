# 杨辉三角形
"""
在屏幕上打印杨辉三角形。杨辉三角形，又称贾宪三角形、帕斯卡三角形，是二项式系数在三角形中的一种几何排列。
"""
# 杨辉三角形，第i行就有i个值，并且第一个和最后一个值都是1，中间的每个值是前一行的两个值的和，比如第4行的第2个数字是第3行的第一个和第二个值的和
def sanjiao(i):
    arr = [0 for i in range(i)]
    if i == 1:
        arr = [1]
    elif i == 2:
        arr = [1,1]
    else:
        arr[0] = 1
        arr[-1] = 1
        for j in range(1,i-1):
            temp = sanjiao(i-1)
            arr[j] = temp[j-1]+temp[j]
    return arr

if __name__ == '__main__':
    for i in range(1,8):
        for j in range(1,7-i+1):
            print(" ",end='')
        print(sanjiao(i))
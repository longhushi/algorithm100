# 阿姆斯特朗数
"""
如果一个整数等于其各个数字的立方和，则该数称为“阿姆斯特朗数”（亦称为自恋性数）。如153=1的立方+5的立方+3的立方就是一个“阿姆斯特朗数”。
试编程求1000以内的所有“阿姆斯特朗数”。
"""
# 这个本质上和水仙花数是一回事
# 循环所有位数，获取各位数字，并求立方和，判断是否等于数字本身
def is_flower(num):
    num = str(num)
    arr = list(num)
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i])**3
    if sum==int(num):
        return True
    return False


if __name__ == '__main__':
    for i in range(1,1000):
        if is_flower(i):
            print("{} 是一个阿姆斯特朗数".format(i))
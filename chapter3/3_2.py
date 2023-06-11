# 水仙花数
"""
输出所有的“水仙花数”。所谓的“水仙花数”是指一个三位数，其各位数字的立方和等于该数本身，例如，153是“水仙花数”，因为153=1的立方+5的立方+3的立方。
"""
# 循环所有三位数，获取各位数字，并求立方和，判断是否等于数字本身
def is_flower(num):
    num = str(num)
    arr = list(num)
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i])**3
    if sum==int(num):
        return True
    return False

print(is_flower(153))

if __name__ == '__main__':
    for i in range(100, 1000):
        if is_flower(i):
            print("{} 是一个水仙花数".format(i))
            
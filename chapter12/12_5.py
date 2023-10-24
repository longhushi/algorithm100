# 填表格
"""
将1、2、3、4、5和6填入下表中，要求每一列右边的数字比左边的数字大且每一行下面的数字比上面的数字大。
编程求出共有几种填写方法？
"""
# 四重循环判断，数组的第一个数字肯定是1，最后一个肯定是6，中间就是四个数字遍历，只要符合要求，且各不相同即可。

def solve():
    arr = [2,3,4,5]
    for i in (arr):
        for j in (arr):
            for k in (arr):
                for z in (arr):
                    if i<j and k<z and i<z and i!=k and j!=z and:
                        print("1, {}, {}, {}, {}, 6".format(i, j, k, z))

if __name__ == '__main__':
    solve()
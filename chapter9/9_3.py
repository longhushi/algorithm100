# 卡布列克常数
"""
对于任意一个4位数n，进行如下的运算：
1）将组成该4位数的4个数字由大到小排列，形成由这4个数字构成的最大的4位数。
2）将组成该4位数的4个数字由小到大排列，形成由这4个数字构成的最小的4位数（如果4个数中含有0，则得到的数不足4位）。
3）求这两个数的差，得到一个新的4位数（高位0保留）。这称为对n进行了一次卡布列克运算。
存在这样一个规律：对一个各位数字不全相同的4位数重复进行若干次卡布列克运算，最后得到的结果总是6174，这个数被称为卡布列克数。
"""
# 递归计算
def compute(n_str):
    arr = list(n_str)
    arr.sort()
    #n2 = str(arr)
    n2 = ''.join(arr)
    arr.sort(reverse=True)
    #n3 = str(arr)
    n3 = ''.join(arr)
    r = int(n3)-int(n2)
    r_str = str(r)
    if len(r_str)<4:
        r_str.ljust(4,'0')
    if r_str=='6174':
        print('prove it!')
        return "6174"
    else:
        return compute(r_str)

if __name__ == '__main__':
    n = "4567"
    compute(n)



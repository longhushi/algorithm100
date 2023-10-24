# 回文数的形成
"""
任取一个十进制正整数，将其倒过来后与原来的正整数相加，会得到一个新的正整数，重复以上步骤，则最终可得到一个回文数。请编程进行验证。
"""
# 定义一个基本函数，实现单次运算，再重复实现这一过程，知道生成回文数

def is_huiwen(num):
    arr = list(str(num))
    for i in range(len(arr)):
        if arr[i] == arr[len(arr)-i-1]:
            pass
        else:
            return False
    return True

def compute(num):
    num_str = str(num)
    l = list(num_str)
    l.reverse()
    num2_str = "".join(l)
    num2 = int(num2_str)
    return num + num2

if __name__ == '__main__':
    num = input("Please enter a number:")
    num = int(num)
    while True:
        num = compute(num)
        if is_huiwen(num):
            print("success, the number is %d" % num)
            break
    
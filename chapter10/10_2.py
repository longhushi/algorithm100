# 奇数平方的有趣性质
"""
任意奇数的平方有这样的有趣性质：任意奇数的平方与1的差是8的倍数。要求编程验证奇数的这个性质。
"""
# 输入一个奇数，计算平方，并减一，看能否整除8
def solve(num):
    square = num**2
    if (square-1)%8==0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    num = input("Please enter an odd number:")
    result = solve(int(num))
    if result == True:
        print("success")
    else:
        print("failure")
# 数制转换
"""
给定一个M进制的数x，实现对x向任意一个非M进制的数的转换
"""
# 先把数x转换为10进制，再转换为另一个进制的数
def convert_to_num(x, base):
    x_arr = list(x)
    x_arr.reverse() # 这里获取到倒序的数字列表，因为要从个位开始处理
    #print(x_arr)
    value = 0
    for i in range(len(x_arr)):
        c = x_arr[i]
        if c.isdigit() and int(c)>=0 and int(c)<=9:
            value = value + int(c)*base**i
        else:
            value = value + (10+ord(c)-ord('A'))*base**i # ord获取到unicode代码，获取到字母和A的差距，而A就是10.
    return value
    
#print(convert_to_num('1001', 2))

def convert_to_other(x, base):
    arr = []
    # 当x可以整除基底的时候，循环获取每一位数字
    while x//base>0:
        c = x%base
        if c>=0 and c<=9:
            c = str(c)
        else:
            chr(ord('A')+(c-10))
        arr.append(c)
        x = x//base
    
    # 单独处理当x不能整除基底的时候
    c = x%base
    if c>=0 and c<=9:
        c = str(c)
    else:
        chr(ord('A')+(c-10))
    arr.append(c)
    return arr

#print(convert_to_other(31, 16))

if __name__ == '__main__':
    base1 = input("Please input the base:")
    num = input("Please enter the num:")
    base2 = input("Please enter the base you want to convert:")
    base1 = int(base1)
    base2 = int(base2)
    value = convert_to_num(num, base1)
    value2 = convert_to_other(value, base2)
    print("after convert, your number will be: ")
    for v in value2:
        print(v,end='')
    print('\n')
    
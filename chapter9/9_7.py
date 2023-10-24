# 逆序输出数字
# 递归实现
def reverse(num_str):
    arr = list(num_str)
    if len(arr) == 1:
        return num_str
    else:
        arr2 = num_str[1:]
        return reverse(arr2)+arr[0]
    
if __name__ == '__main__':
    num_str = "12345"
    print(reverse(num_str))
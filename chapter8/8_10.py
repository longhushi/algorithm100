# 在指定位置插入字符
"""
请编写程序，实现以下功能：在字符串中的所有数字字符前加一个“$”符号。例如，输入A1B23CD45，输出A$1B$2$3CD$4$5。
"""
# 遍历所有字符，如果是数字则在前面加一个$符号
def solve(str):
    result = ""
    for i in range(len(str)):
        if str[i].isdigit():
            result += ('$'+str[i])
        else:
            result += str[i]
    return result

if __name__ == '__main__':
    str = "A1B23CD45"
    print(solve(str))

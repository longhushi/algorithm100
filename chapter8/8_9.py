# 删除*号
"""
现在有一串字符需要输入，规定输入的字符串中只包含字母和“*”符号。请编写程序，实现除了字符串前后的“*”之外，将串中其他的“*”全部删除。
例如，假设输入的字符串为：****A*BC*DEF*G********，删除串中的“*”后，字符串变为：****ABCDEFG********。
"""
# 先取出中间的字符串，然后获取字符串的首尾字母，取得原字符串的前后星号
def solve(str):
    temp = str.replace('*','')
    begin = str[0:str.index(temp[0])]
    end = str[str.index(temp[-1])+1:]
    result = begin + temp + end
    return result

if __name__ == '__main__':
    str = '****A*BC*DEF*G********'
    print(solve(str))

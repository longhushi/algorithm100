# 尼科彻斯定理
"""
尼科彻斯定理可以叙述为“任何一个整数的立方都可以表示成一串连续的奇数的和”
"""
# 输入一个整数，计算该整数的立方，然后从1开始加，如果和超过该数，则停止，从3开始，如此循环
def solve(num):
    trials = num**3
    for i in range(1, trials, 2):
        sum = 0
        arr = []
        for j in range(i, trials, 2):
            sum = sum + j
            arr.append(j)
            if sum == trials:
                print("solved!")
                print(arr)
                return
            elif sum > trials:
                break


if __name__ == '__main__':
    solve(5)
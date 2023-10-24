# 绘制空心菱形
# 分为上下两部分分布打印，上半部分n+1-i,n-1+i打印星号，下半部分，i+1,2*n-1-i打印星号。
def solve(n):
    # 上半部分
    for i in range(1, n+1):
        for j in range(1,n+1-i):
            print(" ",end="")
        print("*",end="")
        if n+1-i==n-1+i:
            print()
        else:
            for j in range(n-i+1, n+i-2):
                print(" ",end="")
            print("*")
    # 下半部分
    for i in range(1, n):
        for j in range(1,i+1):
            print(" ",end="")
        print("*",end="")
        if i+1==2*n-1-i:
            print()
        else:
            for j in range(i+2,2*n-1-i):
                print(" ",end="")
            print("*")


if __name__ == "__main__":
    n = 5
    solve(5)
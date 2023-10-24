# 魔方阵
"""
所谓“n-魔方阵”，指的是使用l～n2共n2个自然数排列成一个n×n的方阵，其中n为奇数。
该方阵的每行、每列以及对角线元素之和都相等，并为一个只与n有关的常数，该常数为n×(n2+1)/2。
编写程序，实现如图8.13所示的5-魔方阵。
1）在第0行中间置1，并对从2开始的其余n2-1个数依次按下面2～5所列规则存放。
2）假定当前数的下标为(i,j)，则下一个数的放置位置为当前位置的右上方，即下标为(i-1,j+1)的位置。
3）如果当前数在第0行，即i-1小于0，则将下一个数放在最后一行的下一列上，即下标为(n-1,j+1)的位置。
4）如果当前数在最后一列上，即j+1大于n-1，则将下一个数放在上一行的第一列上，即下标为(i-1,0)的位置。
5）如果当前数是n的倍数，则将下一个数直接放在当前位置的正下方，即下标为(i+1,j)的位置。
"""
# 根据魔方阵的规则，生成魔方阵，n*n的魔方阵
def solve(n=5):
    arr = [[[]for i in range(n)]for i in range(n)]
    num = 1
    # for i in range(n):
    #     for j in range(n):
    #         if i==0 and j==n/2:
    #             arr[i][j] = num
    #         elif i==0:
    #             arr[n-1][j+1] = 

    for num in range(1,n*n+1):
        if num==1:
            i=0
            j=n//2
            arr[0][n//2]=num
        elif (num-1)%n==0:
                arr[i+1][j] = num
                i = i+1
        elif i==0 and j+1<n:
                arr[n-1][j+1]=num
                i = n-1
                j = j+1
        elif i>0 and j==n-1:
                arr[i-1][0] = num
                i = i-1
                j = 0
        else:
             arr[i-1][j+1] = num
             i = i-1
             j = j+1
    #print(arr)
    print("魔方阵如下：")
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print('\n')


if __name__ == '__main__':
      solve()

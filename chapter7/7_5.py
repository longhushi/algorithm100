# 搬山游戏
"""
设有n座山，计算机与人作为比赛的双方，轮流搬山。规定每次搬山数不能超过k座，谁搬最后一座谁输。
游戏开始时，计算机请人输入山的总数n和每次允许搬山的最大数k，然后请人开始，等人输入了需要搬走的山的数目后，计算机马上打印出它搬多少座山，并提示尚余多少座山。
双方轮流搬山直到最后一座山搬完为止。计算机会显示谁是赢家，并问人是否要继续比赛。如果人不想玩了，计算机便会统计出共玩了几局，双方胜负如何。
"""
# 这个题其实很上一个非常类似，不过是火柴换成了山，并且把具体数字换成了n,k

if __name__ == '__main__':
    n = input("请输入山的总数：")
    k = input("请输入每次搬山不超过多少：")
    n = int(n)
    k = int(k)
    while True:
        x = input("请输入您要搬走的山数目：")
        x = int(x)
        y = k+1-x
        n = n - x - y
        print("计算机搬走{}座山，还剩下{}座山".format(y, n))
        if n==1:
            print("你输了，你要拿走最后一座山")
            break

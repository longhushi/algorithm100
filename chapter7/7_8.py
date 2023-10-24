# 掷骰子
"""
骰子是一个有6个面的正方体，每个面分别印有1～6个小圆点代表点数。
假设这个游戏的规则是两个人轮流掷骰子6次，并将每次投掷的点数累加起来，点数多者获胜，点数相同则为平局。
要求编写程序模拟这个游戏的过程，并求出玩100盘之后谁是最终的获胜者。
"""
# 先写一个比赛的方法，然后主函数中模拟100次，比较胜利次数

import random

def game():
    sum1 = 0
    sum2 = 0
    for i in range(6):
        a = random.randint(1,6)
        b = random.randint(1,6)
        sum1 += a
        sum2 += b
    return sum1,sum2

if __name__ == '__main__':
    c1 = 0 # 玩家1胜利次数
    c2 = 0 # 玩家2胜利次数
    for i in range(100):
        sum1,sum2 = game()
        if sum1>sum2:
            c1 += 1
        elif sum1<sum2:
            c2 += 1
    print("玩家1胜利次数：{}次，玩家2胜利次数：{}次".format(c1,c2))
    if c1>c2:
        print("最终胜者：玩家1")
    elif c1<c2:
        print("最终胜者：玩家2")
    else:
        print("最终平局")
    
# 抢30游戏
"""
由两个人玩“抢30”游戏，游戏规则是：第一个人先说“1”或“1，2”，第二个人要接着往下说一个或两个数，然后又轮到第一个人，再接着往下说一个或两个数。
这样两人反复轮流，每次每个人说一个或两个数都可以，但是不可以连说三个数，谁先抢到30，谁得胜。
"""
# 和前面的思路差不多，反过来推，要抢到30，只要前面抢到27，那么接下来无论对方说28，还是28，29，都是我放胜利，我都可以抢到30，以此类推，前面要能拿到24，21，18，15，12，9，6，3.

if __name__ == '__main__':
    t = 0
    while True:
        num = input('输入你要喊的数字个数：')
        num = int(num)
        if num == 1:
            t = t+1
            print("我要喊两个数字")
            t = t+2
        elif num == 2:
            t = t+2
            print("我要喊一个数字")
            t = t+1
        print(t)
        if t==30:
            print("胜利")
            break
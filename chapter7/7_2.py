# 自动发牌
"""
一副扑克有52张牌，打桥牌时应将牌分给4个人。请设计一个程序完成自动发牌的工作。
要求：黑桃用S（Spaces）表示，红桃用H（Hearts）表示，方块用D（Diamonds）表示，梅花用C（Clubs）表示。
"""
# 构建一个52个元素的列表，从中随机抽取，并减去。
import random
def solve():
    arr = ['1_S','1_H','1_D','1_C',
           '2_S','2_H','2_D','2_C',
           '3_S','3_H','3_D','3_C',
           '4_S','4_H','4_D','4_C',
           '5_S','5_H','5_D','5_C',
           '6_S','6_H','6_D','6_C',
           '7_S','7_H','7_D','7_C',
           '8_S','8_H','8_D','8_C',
           '9_S','9_H','9_D','9_C',
           '10_S','10_H','10_D','10_C',
           '11_S','11_H','11_D','11_C',
           '12_S','12_H','12_D','12_C',
           '13_S','13_H','13_D','13_C']
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    for i in range(13):
        a = random.choice(arr)
        player1.append(a)
        arr.remove(a)
        a = random.choice(arr)
        player2.append(a)
        arr.remove(a)
        a = random.choice(arr)
        player3.append(a)
        arr.remove(a)
        a = random.choice(arr)
        player4.append(a)
        arr.remove(a)
    print("选手1拿到的牌是：{}".format(player1))
    print("选手2拿到的牌是：{}".format(player2))
    print("选手3拿到的牌是：{}".format(player3))
    print("选手4拿到的牌是：{}".format(player4))

if __name__ == '__main__':
    solve()
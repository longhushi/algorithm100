# 双色球
"""
编写程序模拟福利彩票的双色球开奖过程，由程序产生出6个红色球和1个蓝色球。
1）每期开出的红色球号码不能重复，但蓝色球可以是红色球中的一个。
2）红色球的范围是1～33，蓝色球的范围是1～16。
3）输出格式为“红色球：x x x x x x　蓝色球：x”。
"""
# 用random模块解决
import random

def solve():
    red_list = []
    while len(red_list)<6: # 红色球要有六个
        r = random.randint(1,33)
        if r not in red_list: # 因为不能重复，所以如果现在生成随机数已经在列表中了，就不能算
            red_list.append(r)
    b = random.randint(1,16)
    print('红色球：', end=" ")
    for i in range(6):
        print(red_list[i], end=" ")
    print('蓝色球： {}'.format(b))

if __name__ == '__main__':
    solve()
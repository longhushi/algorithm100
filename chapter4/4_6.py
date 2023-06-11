# 歌星大奖赛
"""
在歌星大奖赛中，有10个评委为参赛的选手打分，分数为1～100分。选手最后得分为：去掉一个最高分和一个最低分后其余8个分数的平均值。请编写一个程序实现。
"""
# 把分数存到一个list中，排序，去除首尾两个数字再求平均值
import numpy as np

def score(score_list):
    score_list.sort()
    temp_list = score_list[1:-1]
    return np.mean(temp_list)

if __name__ == '__main__':
    print("请输入评委分数，以逗号分隔：")
    li = input()
    print(li)
    score_list = li.split(",")
    score_list2 = []
    for s in score_list:
        s = int(s)
        score_list2.append(s)
    print(score_list2)
    r = score(score_list2)
    print("歌手得分为：{}".format(r))


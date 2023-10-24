# 选美比赛
"""
用Python语言编写程序完成以下任务：一批选手参加比赛，比赛的规则是最后得分越高，名次越低。
当半决赛结束时，要在现场按照选手的出场顺序宣布最后得分和最后的名次，获得相同分数的选手具有相同的名次，名次连续编号，不用考虑同名次的选手人数。
例如：
选手序号：1，2，3，4，5，6，7
选手得分：5，3，4，7，3，5，6
输出名次为：3，1，2，5，1，3，4
"""
# 把选手的得分存入一个列表，排序，然后改成一个set，并获取每个不重复的元素的索引，索引+1就是名次，因为名次连续编号，所以要用set去重一下。
def solve():
    score_list = [5,3,4,7,3,5,6]
    temp_list = score_list.copy()
    rank_list = []
    
    score_list.sort()
    score_list = list(set(score_list))
    print(score_list)
    for s in temp_list:
        r = score_list.index(s)+1
        rank_list.append(r)
        #print(r)
    print(rank_list)


if __name__ == '__main__':
    solve()
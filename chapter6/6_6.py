# 委派任务
"""
某项任务需要在A、B、C、D、E、F这6个人中挑选人来完成，但挑选人受限于以下条件：
1）A和B两个人至少去一人。
2）A和D不能同时去。
3）A、E和F三人中要挑选两个人去。
4）B和C同时去或者都不去。
5）C和D两人中只能去一个。
6）如果D不去，那么E也不去。
试编程求出应该让哪几个人去完成这项任务。
"""
# 六个循环，随机从列表中选择一个，也可以不选，组成一个列表，判断是否符合要求，等于遍历所有情况
# 不过这种方面太繁琐，还是书上的方法好，每个人只有去或不去，设为0或1，0代表不去，1代表去，把条件表达出来
def solve():
    for a in [0,1]:
        for b in [0,1]:
            for c in [0,1]:
                for d in [0,1]:
                    for e in [0,1]:
                        for f in [0,1]:
                            if a+b>0 and a+d!=2 and a+e+f==2 and (b+c==2 or b+c==0) and c+d==1 and (d+e==0 or d==1):
                                return [a,b,c,d,e,f]

if __name__ == "__main__":
    result = solve()
    print(result)
    li = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(result)):
        if result[i] == 1:
            print('{}去参加任务'.format(li[i]))
        
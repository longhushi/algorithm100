# 谁是窃贼
"""
警察审问4名窃贼嫌疑犯。现在已知，这4人当中仅有一名是窃贼，还知道这4个人中的每个人要么是诚实的，要么总是说谎。
下面是这4个人给警察的回答。·甲说：“乙没有偷，是丁偷的。”·乙说：“我没有偷，是丙偷的。”·丙说：“甲没有偷，是乙偷的。”·丁说：“我没有偷。”
请根据这4个人的回答判断谁是窃贼。
"""
# 设置四个变量判断真假话，然后根据真话判断
def solve():
    for s in ['a','b','c','d']:
        for a in [0,1]:
            for b in [0,1]:
                for c in [0,1]:
                    for d in [0,1]:
                        if ((a==1 and s=='d') or (a==0 and s=='b')) and ((b==1 and s=='c') or (b==0 and s!='c')) and ((c==1 and s=='b')
                         or (c==0 and s=='a')) and ((d==1 and s!='d') or (d==0 and s=='d')):
                            print(s)
                            if s=='a':
                                s = '甲'
                            if s=='b':
                                s = '乙'
                            if s=='c':
                                s = '丙'
                            if s=='d':
                                s = '丁'    
                            print('窃贼是{}'.format(s))

if __name__ == '__main__':
    solve()

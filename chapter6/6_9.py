# 黑与白
"""
有A、B、C、D、E这5个人，每个人额头上都贴了一张黑或白的纸。5人对坐，每个人都可以看到其他人额头上纸的颜色。
A说：“我看见有3人额头上贴的是白纸，1人额头上贴的是黑纸。”
B说：“我看见其他4人额头上贴的都是黑纸。”
C说：“我看见1人额头上贴的是白纸，其他3人额头上贴的是黑纸。”
D说：“我看见4人额头上贴的都是白纸。”
E什么也没说。现在已知额头上贴黑纸的人说的都是谎话，额头上贴白纸的人说的都是实话。
问这5人谁的额头上贴的是白纸，谁的额头上贴的是黑纸？
"""
# 设这五个人，可能位0或1，0代表说谎，1代表说实话。
def solve():
    for a in [0,1]:
        for b in [0,1]:
            for c in [0,1]:
                for d in [0,1]:
                    for e in [0,1]:
                        if ((b+c+d+e==3 and a==1) or (a==0 and b+c+d+e!=3)) \
                            and ((b==1 and a==0 and c==0 and d==0 and e==0) or (b==0 and a+c+d+e>0)) \
                            and ((c==1 and a+b+d+e==1) or (c==0 and a+b+d+e!=1)) \
                            and ((d==1 and a==1 and b==1 and c==1 and e==1) or (d==0 and a+b+c+e<4)):
                            return a, b, c, d, e

if __name__ == '__main__':
    a,b,c,d,e = solve()
    if a==1:
        print('A贴了白纸')
    else:
        print('A贴了黑纸')
    if b==1:
        print('B贴了白纸')
    else:
        print('B贴了黑纸')
    if c==1:
        print('C贴了白纸')
    else:
        print('C贴了黑纸')
    if d==1:
        print('D贴了白纸')
    else:
        print('D贴了黑纸')
    if e==1:
        print('E贴了白纸')
    else:
        print('E贴了黑纸')
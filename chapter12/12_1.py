# 约瑟夫环
"""
17世纪的法国数学家加斯帕在《数目的游戏问题》中讲到一个故事：15个教徒和15个非教徒在深海上遇险，必须将一半的人投入海中，其余的人才能幸免于难。
于是想了一个办法，将30个人围成一个圆圈，从第一个人开始依次报数，每数到第九个人就将他扔入大海，如此循环进行直到仅剩15个人为止。
问怎样的排法才能使每次投入大海的都是非教徒？
"""
# 设计一个列表，由A,B两个值组成，要弹出这个列表每次都是B，最后剩下15个A。其实可以这样想，数到九就把人扔下去，记录序号，这些序号放上B就是正确的排列方式。
def solve():
    result = ['A' for i in range(30)]
    indexs = []
    j=0
    for i in range(15):
        c = 1
        while True:
            if c<9 and result[j]=='A':
                c+=1
                j+=1
                if j>=30:
                    j = j%30
            # elif c<9 and result[j]!='A':
            #     j+=1
            #     if j>=30:
            #         j = j%30
            # elif c==9 and result[j]!='A':
            #     j+=1
            #     if j>=30:
            #         j = j%30
            elif result[j]!='A': # 已经设置为B的，代表已经被扔下海了，直接跳过
                j+=1
                if j>=30:
                    j = j%30
            elif c==9 and result[j]=='A':
                indexs.append(j)
                result[j]='B'
                j+=1
                if j>=30:
                    j = j%30
                break
    print(indexs)
    print(result)
        
if __name__ == '__main__':
    solve()
    print("代号为A的会留在船上，代号为B的会被扔下海，所以只要让非教徒留在B号位置上，就会被都扔下海")
    #[8, 17, 26, 5, 15, 25, 6, 18, 29, 11, 23, 7, 21, 4, 22]
    #['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B']
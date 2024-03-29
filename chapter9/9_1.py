# 猴子吃桃
"""
一个猴子摘了一些桃子，它第一天吃掉了其中的一半然后再多吃了一个，第二天照此方法又吃掉了剩下桃子的一半加一个，
以后每天如此，直到第十天早上，猴子发现只剩下一个桃子了，问猴子第一天总共摘了多少个桃子？
"""
# 用递归方法解决
def peach2(i=10):
    if i == 1: # 到最后一天只剩1个了
        return 1
    else:
        return (peach2(i-1)+1)*2 # 其他时候，早上的桃子都是之后剩下的数量加1再乘以2。反推过来就是总共的桃子数量。

if __name__ == '__main__':
    n = peach2()
    print(n)
# 出售金鱼
"""
小明将养的一缸金鱼分五次出售：第一次卖出全部的一半加1/2条；第二次卖出余下的三分之一加1/3条；第三次卖出余下的四分之一加1/4条；
第四次卖出余下的五分之一加1/5条；最后卖出余下的11条。求出原来鱼缸中有多少条金鱼。
"""
# 用循环求解
# 假设初始有m条鱼，定义一个求剩下的鱼的函数，结果应该等于11
def get_last_num(m):
    last = m
    for i in range(1,5):
        last = last-(last+1)/(i+1)
    return last

if __name__ == '__main__':
    for i in range(20,100): # 从20开始试探
        n = get_last_num(i)
        #print(n)
        if (n)==11:
            print("原来鱼缸中有：{}条鱼".format(i))
            break

    #print("原来鱼缸中有：{}条鱼".format(get_fish_num()))
    

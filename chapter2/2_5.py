# 存钱
"""
现在已知某人手上有2000元，要求通过计算选择一种存钱方案，使得这笔钱存入银行20年后获得的利息最多。假定银行对超出存款期限的那部分时间不付利息。
"""
# 计算每种方案20年可以存几期，然后用复利计算这几期后获得利息总额
# 1年期存x1次，2年期存x2次，3年期存x3次，5年期存x5次，8年期存x8次
def compute_profit(money):
    # money是存款数量，percent是每存一期的利息，num是存款的期数
    profit_list = []
    x_list = []
    x1 = 0 # 1年期存的次数
    x2 = 0 # 2年期存的次数
    x3 = 0 # 3年期存的次数
    x5 = 0 # 5年期存的次数
    x8 = 0 # 8年期存的次数
    for x8 in range(3):
        for x5 in range(5):
            for x3 in range(7):
                for x2 in range(11):
                    x1 = 20-x8*8-x5*5-x3*3-x2*2
                    if x1 < 0:
                        continue
                    #print(x1,x2,x3,x5,x8)
                    profit = money*((1+0.0084*12*8)**x8)*((1+0.0075*12*5)**x5)*((1+0.0069*12*3)**x3)*((1+0.0066*12*2)**x2)*((1+0.0063*12)**x1)
                    #print(profit)
                    x_list.append([x1,x2,x3,x5,x8])
                    profit_list.append(profit)
    #print(profit_list)
    max_profit = max(profit_list)
    max_index = profit_list.index(max_profit)
    return max_profit,x_list[max_index]

if __name__ == "__main__":
    max_profit, x_list = compute_profit(2000)
    max_profit = round(max_profit,2)
    print("最终可以得到{}元，存款方案为：1年期{}次，2年期{}次，3年期{}次，5年期{}次，8年期{}次".format(max_profit,x_list[0],x_list[1],x_list[2],x_list[3],x_list[4]))
    #print(2000*(1+0.0075*12*5)**4)

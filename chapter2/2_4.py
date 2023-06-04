# 个人所得税
"""
编写一个计算个人所得税的程序，要求输入收入金额后，能够输出应缴的个人所得税。
"""
# 主要是选择路径
def get_tax(money):
    tax = 0
    tax_money = money - 2000
    if tax_money <= 0:
        tax = 0
    elif tax_money < 500:
        tax = tax_money*0.05
    elif tax_money < 2000:
        tax = tax_money*0.1
    elif tax_money < 5000:
        tax = tax_money*0.15
    elif tax_money < 20000:
        tax = tax_money*0.2
    elif tax_money < 40000:
        tax = tax_money*0.25
    elif tax_money < 60000:
        tax = tax_money*0.3
    elif tax_money < 80000:
        tax = tax_money*0.35
    elif tax_money < 100000:
        tax = tax_money*0.4
    else:
        tax = tax_money*0.45
    return tax

if __name__ == '__main__':
    money = input('请输入您的收入：')
    money = int(money)
    print("您需要缴的个人所得税是：{}元".format(get_tax(money)))
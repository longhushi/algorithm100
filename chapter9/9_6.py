# 汉诺塔
# 用递归解决
def move(n,a,b,c):
    if n==1:
        print("move %d from %s to %s" % (n,a,c))
    else:
        move(n-1,a,c,b) # 借助C杆移动到B杆
        print("move %d from %s to %s" % (n-1,a,b))
        move(n-1,b,a,c) # B借助C杆移动到A杆

if __name__ == "__main__":
    n = 5
    move(5,"a","b","c") # 移动又五个圆盘组成的汉诺塔
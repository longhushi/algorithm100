# 分糖果
"""
10个小孩围成一圈分糖果，老师分给第1个小孩10块，第2个小孩2块，第3个小孩8块，第4个小孩22块，第5个小孩16块，第6个小孩4块，第7个小孩10块，第8个小孩6块，第9个小孩14块，第10个小孩20块。
然后所有的小孩同时将手中的糖分一半给右边的小孩；糖块数为奇数的人可向老师要一块。问经过这样几次后大家手中的糖一样多？每人各有多少块糖？
"""
# 本题其实一个链表结构。构建一个列表，遍历列表
cookie_list = [10,2,8,22,16,4,10,6,14,20]

def is_equal(cookie_list):
    a = cookie_list[0]
    for i in cookie_list:
        if i != a:
            return False
    return True


def solve():
    # 设置遍历100次，足够了
    for i in range(100):
        # 糖果为奇数的可以再加一块
        for i in range(len(cookie_list)):
            if cookie_list[i] % 2 == 1:
                cookie_list[i] += 1
        #print(cookie_list)
        c = [cookie//2 for cookie in cookie_list] # 获取到每次可以分配的糖果数
        # 开始分配
        for i in range(len(cookie_list)):
            if i==9:
                cookie_list[0] += c[9]
                cookie_list[9] -= c[9] # 送出糖果的小孩自己的糖果数减半
            else:
                cookie_list[i+1] += c[i] # 右边的小孩得到前面的小孩手里的一半糖果
                cookie_list[i] -= c[i] # 送出糖果的小孩自己的糖果数减半
            
        print(cookie_list)
        if is_equal(cookie_list):
            print("大家手中的糖果一样多了")
            print("经过了{}次分配，每人手中有{}块糖".format(i+1, cookie_list[0]))
            break
    
if __name__ == '__main__':
    solve()

# 求车速
"""
一辆以固定速度行驶的汽车，司机在上午10点看到里程表上的读数是一个对称数，为95859。两小时后里程表上出现了一个新的对称数，该数仍为5位数。
问该车的速度是多少？新的对称数是多少？
"""
# 这个题目先要求出新的对称数，相减就是距离，就可以计算速度了
def is_duichen_num(n):
    arr = list(n)
    for i in range(len(arr)):
        c = arr[i]
        if arr[i]!=arr[len(arr)-i-1]:
            return False
    return True

print(is_duichen_num('95859'))

def solve():
    for i in range(95860, 99999):
        if is_duichen_num(str(i)):
            distance = i - 95859
            v = distance/2
            print("该车的速度是：{}km/h，新的对称数是：{}".format(v, i))
            break
    
if __name__ == '__main__':
    solve()
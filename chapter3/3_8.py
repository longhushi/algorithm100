# 黑洞数
"""
黑洞数又称陷阱数，是指任何一个数字不全相同的整数，在经过有限次“重排求差”操作后，总会得到某一个或一些数，这些数即为黑洞数。
“重排求差”操作是将组成一个数的各位数字重排，将得到的最大数减去最小数。
例如，207的“重排求差”操作序列是：720-027=693，963-369=594，954-459=495，此时再进行“重排求差”操作不会发生改变。
再用208计算一次，也是停止到495，所以495是三位黑洞数。
"""
# 先定义两个函数，一个求一堆数字所能组成的最大值，一个求一堆数字所能组成的最小值，然后一个函数求差，不断循环，当这个差不再变化的时候，就是黑洞数

def get_max(num_list):
    a = len(num_list)
    num = ''
    for i in range(a):
        num += str(max(num_list))
        num_list.remove(max(num_list))
    return int(num)

def get_min(num_list):
    a = len(num_list)
    num = ''
    for i in range(a):
        num += str(min(num_list))
        num_list.remove(min(num_list))
    return int(num)

print(get_max(['2','7','0']))
print(get_min(['2','7','0']))

def get_sub(num):
    num = str(num)
    sub = get_max(list(num))-get_min(list(num))
    return sub

if __name__ == '__main__':
    blackhole_old = 1800
    while True:
        blackhole = get_sub(blackhole_old)
        if blackhole == blackhole_old: # 如果不再改变，则说明找到了黑洞数
            break
        else:
            blackhole_old = blackhole

    print("{}是一个黑洞数".format(blackhole))
    
        


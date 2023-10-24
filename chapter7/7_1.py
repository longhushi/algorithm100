# 黑白子交换
"""
用最少的步数将图7.1中白子和黑子的位置进行交换
游戏的规则如下：
1）一次只能移动一个棋子。
2）棋子可以向空格中移动，也可以跳过一个对方的棋子进入空格。
3）白色棋子只能向右移动，黑色棋子只能向左移动，不能跳过两个棋子。
"""
import random
# 定义一个列表，['w','w','w','s','b','b','b']，希望得到结果['b','b','b','s','w','w','w']
# w和b可以移动到s，也可以跳过一个对方棋子到s
def solve():
    arr = ['w','w','w','s','b','b','b']
    while arr!=['b','b','b','s','w','w','w']:
        print(arr)
        if arr == ['b','b','b','s','w','w','w']:
            print('success')
            return
        if(block(arr)):
            print('阻塞了，重新开始')
            #arr = ['w','w','w','s','b','b','b']
            #continue
            return
        i = arr.index('s')
        selects = []
        '''
        if (arr[i]=='s' and arr[i+1]=='b' and i+1<len(arr)):
            # 交换
            arr[i] = 'b'
            arr[i+1] = 's'
            print("move:{}的b移动到{}".format(i+1,i))
        elif (arr[i]=='s' and arr[i+1]=='w' and arr[i+2]=='b' and i+2<len(arr)):
            # 交换
            arr[i] = 'b'
            arr[i+2] = 's'
            print("move:{}的b移动到{}".format(i+2,i))
        elif (arr[i]=='s' and arr[i-1]=='w' and i-1>=0):
            # 交换
            arr[i] = 'w'
            arr[i-1] = 's'
            print("move:{}的w移动到{}".format(i-1,i))
        elif (arr[i]=='s' and arr[i-1]=='b' and arr[i-2]=='w' and i-2>=0):
            # 交换
            arr[i] = 'w'
            arr[i-2] = 's'
            print("move:{}的w移动到{}".format(i-2,i))
        '''
        if (i+1<len(arr) and arr[i]=='s' and arr[i+1]=='b'):
            selects.append(1)
        if (i+2<len(arr) and arr[i]=='s' and arr[i+1]=='w' and arr[i+2]=='b'):
            selects.append(2)
        if (i-1>=0 and arr[i]=='s' and arr[i-1]=='w'):
            selects.append(3)
        if (i-2>=0 and arr[i]=='s' and arr[i-1]=='b' and arr[i-2]=='w'):
            selects.append(4)
        c = random.choice(selects)
        if c==1:
           # 交换
            arr[i] = 'b'
            arr[i+1] = 's'
            print("move:{}的b移动到{}".format(i+1,i))
        if c==2:
           # 交换
            arr[i] = 'b'
            arr[i+2] = 's'
            print("move:{}的b移动到{}".format(i+2,i))
        if c==3:
           # 交换
            arr[i] = 'w'
            arr[i-1] = 's'
            print("move:{}的w移动到{}".format(i-1,i))
        if c==4:
           # 交换
            arr[i] = 'w'
            arr[i-2] = 's'
            print("move:{}的w移动到{}".format(i-2,i))
    print("解决了！")
                    
    

# 定义阻塞函数
def block(arr):
    # 如果两个w都在s左边且连在一起就阻塞了，如果两个b都在s右边且连在一起也阻塞了。
    k = arr.index('s')
    for i in range(len(arr)):
        if i+1<len(arr) and i+1<k and arr[i]=='b' and arr[i+1]=='b':
            return True
        elif i+1<len(arr) and arr[i]=='w' and arr[i+1]=='w' and i>k:
            return True
    return False

    
def move(arr):
    if arr==['b','b','b','s','w','w','w']:
        print("success!")
        return
    
    # 如果两个w都在s左边且连在一起就阻塞了，如果两个b都在s右边且连在一起也阻塞了。
    if block(arr):
        print("block!")
        return

    i = arr.index('s')
    if (arr[i]=='s' and arr[i+1]=='w' and i+1<len(arr)):
        # 交换
        arr[i] = 'w'
        arr[i+1] = 's'
        print("move:{}的w移动到{}".format(i+1,i))
    elif (arr[i]=='s' and arr[i+1]=='b' and arr[i+2]=='w' and i+2<len(arr)):
        # 交换
        arr[i] = 'w'
        arr[i+2] = 's'
        print("move:{}的w移动到{}".format(i+2,i))
    elif (arr[i]=='s' and arr[i-1]=='b' and i-1>=0):
        # 交换
        arr[i] = 'b'
        arr[i-1] = 's'
        print("move:{}的b移动到{}".format(i-1,i))
    elif (arr[i]=='s' and arr[i-1]=='w' and arr[i-2]=='b' and i-2>=0):
        # 交换
        arr[i] = 'b'
        arr[i-2] = 's'
        print("move:{}的b移动到{}".format(i-2,i))
    move(arr)


# 书上的方法是把所有可能的走动路线列出来
def solve2():
    arr = ['w','w','w','s','b','b','b']
    #while (arr[0]!='b' or arr[1]!='b' or arr[2]!='b') or (arr[4]!='w' or arr[5]!='w' or arr[6]!='w'):
    while arr!=['b','b','b','s','w','w','w']:
        #print('now arr:{}'.format(arr))
        flag = True # True表示还没有移动过棋子，False表示已经移动过
        i = 0
        while flag and i<5:
            # 若白子可以向右跳过黑子则白子向右跳
            if arr[i]=='w' and arr[i+1]=='b' and arr[i+2]=='s':
                arr = change(arr,i,i+2)
                print(arr)
                flag = False
            i+=1
        i = 0
        while flag and i<5:
            # 若黑子可以向左跳过白子则黑子向左跳
            if arr[i]=='s' and arr[i+1]=='w' and arr[i+2]=='b':
                arr = change(arr,i,i+2)
                print(arr)
                flag = False
            i+=1
        i = 0
        while flag and i<6:
            # 若向右移动白子不会产生阻塞，则白子向右移动
            f = True
            if i<5:
                f = arr[i-1]!=arr[i+2] # 表示不是两个相同颜色的相邻
            if arr[i]=='w' and arr[i+1]=='s' and (i==0 or f):
                arr = change(arr, i, i+1)
                print(arr)
                flag = False
            i+=1
        i = 0
        while flag and i<6:
            # 若向左移动黑子不会产生阻塞，则黑子向左移动
            f = True
            if i<5:
                f = arr[i-1] != arr[i+2] # 表示不是两个相同颜色的相邻
            if arr[i]=='s' and arr[i+1]=='b' and (i==5 or f):
                arr = change(arr, i, i+1)
                print(arr)
                flag = False
            i += 1

def change(arr,i,j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    return arr
        
        
if __name__ == '__main__':
    #arr = ['w','w','w','s','b','b','b']
    #move(arr)
    solve2()
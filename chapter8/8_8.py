# 马踏棋盘
"""
国际象棋的棋盘为8×8的方格棋盘。现将“马”放在任意指定的方格中，按照“马”走棋的规则将“马”进行移动。
要求每个方格只能进入一次，最终使得“马”走遍棋盘的64个方格。
编写一个Python程序，实现马踏棋盘操作，要求用1～64这64个数字标注“马”移动的路径，也就是按照求出的行走路线，将数字1～64依次填入棋盘的方格中，并输出。
"""
# 相当于将1~64填入到一个8*8的矩阵中。例如数字a放置在矩阵的(i,j)位置上，
# 则数字a+1只能放置在矩阵的(i-2,j+1)、(i-1,j+2)、(i+1,j+2)、(i+2,j+1)、(i+2,j-1)、(i+1,j-2)、(i-1,j-2)、(i-2,j-1)之中的一个位置上。

def travel(x, y, tag, chess,X, Y):
    x1, y1, flag, count = x, y, False, 0
    chess[x][y] = tag
    if tag == 60:
        return True # 搜索成功，返回1
    flag,x1,y1 = nextxy(x1,y1,count, X, Y, chess) #找到基于x1,y1的下一步可走位置
    # 上一步如果未找到，则在剩下的步骤中找
    while not flag and count<7:
        count += 1
        print('(1):',count)
        flag,x1,y1 = nextxy(x1,y1,count, X, Y, chess)
    # 找到下一个可走的位置，则进行深度优先搜索
    while flag:
        if travel(x1, y1, tag+1, chess, X, Y):
            return True
        x1 = x
        y1 = y
        count = count+1
        flag, x1, y1 = nextxy(x1,y1,count, X, Y, chess) # 寻找下一个位置
        while not flag and count<7:
            count += 1
            print('(2):',count)
            flag,x1,y1 = nextxy(x1,y1,count, X, Y, chess)
    if not flag:
        chess[x][y] = 0 # 搜索不成功，擦除足迹
    return False

# 找到基于x,y下一个可走的位置
def nextxy(x, y, count, X, Y, chess):
    if count==0 and x+2<=X-1 and y-1>=0 and chess[x+2][y-1]==0:
        x = x+2
        y = y-1
        flag = True
    elif count==1 and x+2<=X-1 and y+1<=Y-1 and chess[x+2][y+1]==0:
        x = x+2
        y = y+1
        flag = True
    elif count==2 and x+1<=X-1 and y-2>=0 and chess[x+1][y-2]==0:
        x = x+1
        y = y-2
        flag = True
    elif count==3 and x+1<=X-1 and y+2<=Y-1 and chess[x+1][y+2]==0:
        x = x+1
        y = y+2
        flag = True
    elif count==4 and x-2>=0 and y-1>=0 and chess[x-2][y-1]==0:
        x = x-2
        y = y-1
        flag = True
    elif count==5 and x-2>=0 and y+1<=Y-1 and chess[x-2][y+1]==0:
        x = x-2
        y = y+1
        flag = True
    elif count==6 and x-1>=0 and y-2>=0 and chess[x-1][y-2]==0:
        x = x-1
        y = y-2
        flag = True
    elif count==7 and x-1>=0 and y+2<=Y-1 and chess[x-1][y+2]==0:
        x = x-1
        y = y+2
        flag = True
    else:
        flag = False
    return flag,x,y

if __name__ == '__main__':
    X = 6
    Y = 6
    chess = [[0]*X for i in range(Y)] # 初始化，棋盘所有位置都置为0
    if travel(0,0,1,chess,X,Y): # 深度优先搜索
        for i in range(X):
            for j in range(Y):
                print("%-5d"%chess[i][j],end='')
            print()
        print("success")
    else:
        print("failure")



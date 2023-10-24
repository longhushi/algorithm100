# 谁在说谎
"""
现有张三、李四和王五三个人，张三说李四在说谎，李四说王五在说谎，而王五说张三和李四两人都在说谎。
要求编程求出这三个人中到底谁说的是真话，谁说的是假话。
"""
# 把三个变量的情况都列出来,x代表张三，y代表李四，z代码王五，都有0和1两种状态
def solve():
    for x in [0,1]:
        for y in [0,1]:
            for z in [0,1]:
                if ((x==1 and y==0) or (x==0 and y==1)) and ((y==1 and z==0) or (y==0 and z==1)) and((z==1 and x+y==0) or (z==0 and x+y!=0)):
                    print(x,y,z)
                    if x==1:
                        print('张三说的是真话')
                    else:
                        print('张三说的是假话')
                    if y==1:
                        print('李四说的是真话')
                    else:
                        print('李四说的是假话')
                    if z==1:
                        print('王五说的是真话')
                    else:
                        print('王五说的是假话')
    
if __name__ == "__main__":
    solve()
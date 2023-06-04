# 猜牌数
"""
魔术师利用一副牌中的13张黑桃，预先将它们排好后叠在一起，并使牌面朝下。然后他对观众说：我不看牌，只要数数就可以猜到每张牌是什么，我大声数数，你们听，不信你们就看。
魔术师将从最上面的一张牌开始数，第一张把它翻过来正好是黑桃A，他将黑桃A放在桌子上，然后按顺序从上到下数手中的余牌，
第二次数1、2，将第一张牌放在这叠牌的下面，将第二张牌翻过来，正好是黑桃2，也将它放在桌子上，
第三次数1、2、3，将前面两张依次放在这叠牌的下面，再翻第三张牌正好是黑桃3，这样依次进行，将13张牌全部翻出来，准确无误。
问魔术师手中的牌原始次序是怎样安排的？
"""
# 设置一个数组,长度为13，都为0，当轮到i时，从当前开始数i个数，把i设置到相应位置，剩下的列表继续循环，同时跳过不为0的数字，不参与计数。
"""
算法伪代码：
如果等于零则计数，否则就跳过
数字如果到达13了则归零，c重新从零开始计数。
定义一个变量，用来存放经过的零的个数，每经过一个就加一（第一个除外），放2要经过1个零，放3要经过2个零，放4要经过3个零，以此类推。
第一个循环，遍历1到13，
第二个循环，如果还没有放下，可以用一个标志位表示，就一直循环这个init_list，
while  !flag:
  #增加零数，对零计数
  i++
  if i==13:
   i=0
  if 零的个数=外循环的索引：
     #设置初始表
     flag=true
     break
   记录i   
"""

def get_order():
    init_list = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    current = 0
    for i in range(1,14):
        for j in range(1,14):
            if current <= 13:
                if init_list[current]==0:
                    init_list[current] = i 
                    current = current+j+1
                else:
                    #current += 1 # 往后推一位
                    #init_list[current] = i 
                    pass
            else:
                current = current%13+1
                if init_list[current]==0:
                    init_list[current] = i 
                    current = current+j+1
                else:
                    #current += 1 # 往后推一位
                    #init_list[current] = i 
                    pass

        print(init_list)
    print(init_list)

def get_order2():
    init_list = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    flag_list = [False,False,False,False,False,False,False,False,False,False,False,False,False]
    current = 0
    for i in range(1,14):
        zeros = 0
        while flag_list[i-1]==False:
            if zeros == i-1:
                flag_list[i-1] = True
                while init_list[current]!=0: # 只有零的位置才能放
                    current += 1
                init_list[current] = i
                current += 1
                continue
            else:
                # 对零计数
                if init_list[current]==0:
                    zeros += 1
                    current += 1
                else:
                    current += 1
                if current == 13:
                    current = 0
        print(init_list)
        print(flag_list)    

        
if __name__ == "__main__":
    get_order2()


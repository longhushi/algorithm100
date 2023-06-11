# 谁家孩子跑的慢
"""
假设有张、王、李三家，每家都有3个孩子。某一天，这三家的9个孩子一起短跑比赛，规定不考虑年龄大小，第一名得9分，第二名得8分，第三名得7分，以此类推。
比赛结束后统计分数发现三家孩子的总分是相同的，同时限定这9个孩子的名次不存在并列的情况，且同一家的孩子不会获得相连的名次。
现已知获得第一名的是李家的孩子，获得第二名的是王家的孩子，要求编程求出获得最后一名的是哪家的孩子。
"""
# 其实就一个列表，包含9个数字，其中每3个数的和是相等的，求这三个数分布。
def solve():
    li = [7,6,5,4,3,2,1]
    s = sum(li)
    score = s//3 # 因为分数相同，所以每一家的分数都是15分
    z_list = []
    w_list = [8]
    l_list = [9]
    for i in range(len(li)):
        for j in range(i,len(li)):
            if (li[i]+li[j])==6:
                for a in range(len(li)):
                    for b in range(a, len(li)):
                        if (li[a]+li[b])==7 and a!=i and a!=j and b!=i and b!=j:
                            l_list.append(li[i])
                            l_list.append(li[j])
                            w_list.append(li[a])
                            w_list.append(li[b])
                            #print(l_list)
                            #print(w_list)
                            return (l_list,w_list)
                            # li.remove(li[i])
                            # li.remove(li[j])
                            # li.remove(li[a])
                            # li.remove(li[b])
    

    
    

if __name__ == '__main__':
    l_list,w_list = solve()
    z_list = list(set([9,8,7,6,5,4,3,2,1])-set(w_list)-set(l_list))
    print(w_list)
    print(l_list)
    print(z_list)
    if 1 in z_list:
        print("最后一名是张家的孩子")
    elif 1 in w_list:
        print("最后一名是王家的孩子")
    else:
        print("最后一名是李家的孩子")




    


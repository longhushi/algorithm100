# 不重复的三位数
"""
用1、2、3、4共4个数字能组成多少个互不相同且无重复数字的三位数？都是多少？
"""
# 从四个数字中选择三个组成一个三位数，放入一个set中
def get_num(list):
    num_list = []
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                num = ''
                if i!=j and j!=k and i!=k:
                    num = num+str(i)+str(j)+str(k)
                    num_list.append(int(num))
    return num_list

if __name__=='__main__':
    li = []
    li = get_num([1,2,3,4])
    li=list(set(li))
    print("可以组成{}个三位数，分别是{}".format(len(li),li))
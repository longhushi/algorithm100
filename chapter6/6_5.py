# 旅客的国籍
"""
在一个旅馆中住着6个不同国籍的人，他们分别来自美国、德国、英国、法国、俄罗斯和意大利。
他们的名字分别叫A、B、C、D、E和F，要说明的是名字的顺序与前面提到的国籍不一定是相互对应的。
现在已知：
1）A和美国人是医生。
2）E和俄罗斯人是教师。
3）C和德国人是技师。
4）B和F曾经当过兵，而德国人从未参过军。
5）法国人比A年龄大，意大利人比C年龄大。
6）B同美国人下周要去西安旅行，而C同法国人下周要去杭州度假。
现要求根据上述已知条件，编程求出A、B、C、D、E和F各是哪国人。
"""
# A不是美国人，也不是法国人，也不是德国人（职业不同），也不是俄罗斯人（职业不同）；B不是美国人也不是德国人也不是法国人；C不是美国人也不是德国人也不是意大利人也不是法国人也不是俄罗斯人（职业不同）；
# E不是俄罗斯人，不是美国人（职业不同），也不是德国人（职业不同）；F不是德国人
def solve():
    # 假设国籍列表1——美国，2——德国，3——英国，4——法国，5——俄罗斯，6——意大利
    a_list = [3,6]
    b_list = [3,5,6]
    c_list = [3]
    d_list = [1,2,3,4,5,6]
    e_list = [3,4,6]
    f_list = [1,3,4,5,6]
    for d in d_list:
        for e in e_list:
            for f in f_list:
                for a in a_list:
                    for b in b_list:
                        for c in c_list:
                            li = [a,b,c,d,e,f]
                            if len(set(li))==6: # 因为set里面没有重复元素，用这种方法表示li中的六个元素都是各自不同的，也就是有正确的位置的
                                return [a,b,c,d,e,f]

if __name__ == '__main__':
    result = solve()
    print(result)
    d = {1:'美国',2:'德国',3:'英国',4:'法国',5:'俄罗斯',6:'意大利'}
    print('A是{}人'.format(d[result[0]]))
    print('B是{}人'.format(d[result[1]]))
    print('C是{}人'.format(d[result[2]]))
    print('D是{}人'.format(d[result[3]]))
    print('E是{}人'.format(d[result[4]]))
    print('F是{}人'.format(d[result[5]]))


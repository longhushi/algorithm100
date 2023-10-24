# 求出符合要求的素数
"""
编写程序实现将大于某个整数n且紧靠n的k个素数存入某个数组中，
同时实现从infile.txt文件中读取10对n和k的值，分别求出符合要求的素数，
并将结果保存到outfile.txt文件中。
"""
# 需要先读取文件，再计算，最后写入文件
def solve():
    out = open('outfile.txt', 'a')
    f = open('infile.txt')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        n = line.split(',')[0]
        k = line.split(',')[1]
        n = int(n)
        k = int(k)
        su_list = get_su(n, k)
        out.write(str(su_list))
        out.write('\n')
    out.close()


def is_su(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True

def get_su(n, k):
    su_list = []

    while len(su_list)<k:
        n+=1
        if is_su(n):
            su_list.append(n)
    return su_list

if __name__ == '__main__':
    solve()

# 借书方案知多少
"""
小明有5本新书，要借给A、B、C三位小朋友，若每人每次只能借1本，则可以有多少种不同的借法？
"""
# 用三重循环解决
def borrow_book():
    print("借书方案：")
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if(j!=i and k!=j and k!=i):
                    print("A: {}, B: {}, C: {}".format(i+1,j+1,k+1)) # 因为range函数从0开始，借书的序号从1开始，所以要加1

if __name__ == '__main__':
    borrow_book()
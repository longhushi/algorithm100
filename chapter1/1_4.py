# 百钱百鸡
"""
中国古代数学家张丘建在他的《算经》中提出了一个著名的“百钱百鸡”问题：一只公鸡值五钱，一只母鸡值三钱，三只小鸡值一钱，现在要用百钱买百鸡，
请问公鸡、母鸡、小鸡各多少只？
"""
# 因为要买百鸡，所以有个约束就是三种鸡加一起数量是100，价格加起来也是100
def solve():
    # 因为公鸡五钱，所以公鸡最多不会超过20只，因为母鸡三钱，所以母鸡最多不会超过33只
    for i in range(20):
        for j in range(33):
            if (5*i + 3*j + (100-i-j)/3)==100:
                print("百钱买百鸡，可以买公鸡：{}只，母鸡{}只，小鸡{}只".format(i,j,(100-i-j)))
                continue

if __name__ == '__main__':
    solve()
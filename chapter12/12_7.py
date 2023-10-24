# 统计学生成绩
"""
有5个学生，每个学生有三门课程的成绩需要统计。
要求从键盘输入学生的学号、姓名以及三门课程的成绩，计算出平均成绩，并将原有的数据和计算出的平均成绩存放在磁盘文件stud中。
"""
# 键盘输入并存储到文件
def solve():
    #stu_list = []
    i = 0
    out = open('stu.txt', 'a')
    while i<5:
        num = input("请输入学生学号：\n")
        name = input("请输入学生姓名：\n")
        score1 = input("请输入第一门考试的分数：\n")
        score2 = input("请输入第二门考试的分数：\n")
        score3 = input("请输入第三门考试的分数：\n")
        avg = (float(score1)+float(score2)+float(score3))/3
        avg = str(avg)
        out.write("学生学号："+num+"\n")
        out.write("学生姓名："+name+"\n")
        out.write("学生成绩1："+score1+"\n")
        out.write("学生成绩2："+score2+"\n")
        out.write("学生成绩3："+score3+"\n")
        out.write("学生平均分："+avg+"\n")
        i+=1
    out.close()

if __name__ == '__main__':
    solve()
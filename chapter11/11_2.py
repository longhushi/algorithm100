# 画圆和圆弧
"""
用turtle画一个笑脸
"""
# @author zhangjian
# @description 画笑脸
import turtle

if __name__ == '__main__':
    # 画脸
    turtle.width(2)
    turtle.color("black")
    turtle.circle(120)

    # 画眼睛
    turtle.penup()
    turtle.goto(-60, 130)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(20)

    turtle.penup()
    turtle.goto(60, 130)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(20)

    # 画鼻子
    turtle.penup() # 抬笔
    turtle.goto(0, 120) # 移动到坐标点
    turtle.pendown() # 下笔
    turtle.goto(-50, 70)
    turtle.goto(50, 70)
    turtle.goto(0, 120)

    # 画嘴巴
    turtle.penup() # 抬笔
    turtle.goto(-60, 45) 
    turtle.pendown()
    turtle.setheading(90) # 设置朝向
    len = 1 # 初始走的速度为1
    for j in range(60):
        if j>30: # 当j<30，也就是画前一半的弧线
            len += 0.2 # 让速度越走越快
        else:
            len -= 0.2 # 让速度越走越慢
        turtle.forward(len) # 前进
        turtle.left(3) # 左转
    turtle.goto(-60, 45)

    turtle.done() # 关闭



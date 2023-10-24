# 填充彩色图形
#@author zhangjian
#@desc 填充彩色图形
import turtle
import time

if __name__ == "__main__":
    t = turtle.Pen() # 启动画笔
    t.color('green','pink') # 设置颜色
    t.hideturtle() # 隐藏海龟
    t.begin_fill() # 开始填充颜色
    for x in range(3):
        t.forward(180) # 前进
        t.left(180-60) # 左转
    t.forward(10) # 直行10个像素
    t.right(90) # 右转90度
    t.end_fill() # 填充结束

    t.color('green','brown')
    t.begin_fill()
    for x in range(3):
        t.forward(160)
        t.left(90)
    t.end_fill()

    t.penup() # 抬笔
    t.goto(30, -160) 
    t.pendown() # 落笔

    for x in range(3):
        t.right(90)
        t.forward(40)

    t.penup()
    t.color('green', 'red')
    t.begin_fill()
    t.goto(100, 200)
    t.circle(20) # 画圆
    t.end_fill()

    time.sleep(20)

 
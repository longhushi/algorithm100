# 画直线
"""
用Python自带的turtle模块画图
"""
# @author zhangjian
# @desc 画直线

import turtle

if __name__ == "__main__":
    # 绘制折线
    turtle.penup() # 提笔
    turtle.color('green','red')
    turtle.goto(100, 100)
    turtle.pendown() # 落笔

    turtle.goto(100, -100)
    turtle.goto(-100, -100)
    turtle.goto(-100, 100)
    turtle.goto(100, 100)
    turtle.goto(5, 125)
    turtle.goto(-108, 90)

    turtle.done()
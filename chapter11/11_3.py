# 画彩色图形
"""
用turtle绘制一个彩色的六边形，可以使用一个颜色列表，为这个六边形设置多种颜色
"""
# 使用一个for循环来实现绘制六边形，让画笔不停地绘制，同时这个六边形会逐渐变大。
# 在for循环内设置画笔的颜色，使得每条边都是不同的颜色，并且随着循环次数的不断增加，画笔不断地前进、左转，同时画笔宽度也在不断变化。

# @author zhangjian
# @desc 画彩色图形

import turtle

if __name__ == '__main__':
    t = turtle.Pen() # 启用画笔
    turtle.bgcolor("white") # 设置画板背景色
    sides = 6 # 图形边数
    colors = ["red","yellow","green","blue","orange","purple"] # 颜色列表
    for x in range(360):
        t.pencolor(colors[x%sides]) # 设置画笔颜色
        t.forward(x*3/sides+x) # 前进
        t.left(360/sides+1) # 左转
        t.width(x*sides/200) # 画笔宽度

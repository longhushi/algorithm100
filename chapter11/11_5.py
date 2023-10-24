# 绘制空心圆
"""
根据圆的参数方程来画圆
"""
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']    # 用于正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号

    r = 2.0 # 半径
    a,b = (0,0) # 圆心
    # 参数方程
    circle = np.arange(0, 2*np.pi, 0.01)
    x = a+r*np.cos(circle) 
    y = b+r*np.sin(circle)
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x,y)
    axes.axis('equal')
    plt.title('圆形')
    plt.show()
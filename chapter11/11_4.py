# 绘制余弦曲线
"""
要绘制余弦函数曲线，需要使用到Python语言的NumPy库和matplotlib库，绘制的余弦函数曲线在0～360°（2π）的范围内。
"""
# @author zhangjian
# @desc 绘制余弦曲线

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']    # 用于正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号
    # 范围0~2pi，共100等分
    X = np.linspace(0, 2*np.pi, 100) # 生成指定大小的一维数组
    Y = np.cos(X) # 得到余弦值
    plt.plot(X, Y, 'g', linewidth=4) # 传入数据，设置线宽和颜色
    plt.title('余弦曲线图')
    #plt.savefig('result1.png') # 保存图片
    plt.show()

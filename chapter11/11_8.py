# 绘制饼状图
#@author zhangjian
#@desc 绘制饼状图

import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 用于正常显示中文标签
    labels = ['苹果','香蕉','雪梨','西瓜','葡萄']
    sizes = [10, 15, 8, 62, 5]
    explode = (0,0,0,0.1,0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels = labels, autopct='%1.1f%%', shadow=True, startangle=90) # 绘制饼状图
    ax1.axis('equal') # 保证饼图绘制出来以后是圆形
    plt.title('水果销量图')
    plt.show()
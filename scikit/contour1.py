# -*- coding:utf-8 -*-
#引入numpy库和matplotlib库
import numpy as np
import matplotlib.pyplot as plt

# 定义等高线图的横纵坐标x，y
#从左边取值为从 -3 到 3 ，各取5个点，一共取 5*5 = 25 个点
x = np.linspace(-3, 3, 5)
y = np.linspace(-3, 3, 5)
# 将原始数据变成网格数据
X, Y = np.meshgrid(x, y)

# 各地点对应的高度数据
#Height是个 5*5 的数组，记录地图上 25 个点的高度汇总
Height = [[0,0,1,2,2],[0,-2,-2,1,5],[4,2,6,8,1],[3,-3,-3,0,5],[1,-5,-2,0,3]]

# 填充颜色
area = 10
plt.contourf(X, Y, Height, area, alpha = 0.6, cmap = plt.cm.hot)
# 绘制等高线
C = plt.contour(X, Y, Height, 10, colors = 'black')#, linewidth = 0.5)
# 显示各等高线的数据标签
plt.clabel(C, inline = True, fontsize = 10)
# 去除坐标轴
plt.xticks(())
plt.yticks(())
plt.show()
"""
contourf 填充颜色函数

前三个参数 X, Y, Height 用来引进点的位置和对应的高度数据；
数字 10 代表将等高线图分成10块（这里不是硬性要求，但数值过小会造成部分分区颜色区分度不高）；
alpha = 0.6 用来设置填充颜色的范围，alpha取值为 [0,1) 。alpha=0时，画出的是无色图，alpha越接近1，
颜色的搭配就越向深色风格过渡
contour 绘制等高线函数

前面的参数跟contourf一样；
colors = ‘black’ 代表线条颜色是黑色；
linewidth = 0.5 代表线条粗细

如果遇到不能靠单纯输入各点高度值的情况，就需要将Height数组变成一个以横纵坐标X和Y为参数的高度计算函数：

def f(x, y):
    return x * y #这里的函
"""
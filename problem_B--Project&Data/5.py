# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 02:59:04 2020

@author: 11854
"""
import numpy as np
import pandas as pd
df = pd.read_csv("result_S_RON.csv",header = None) #读取训练集csv文件,新的y_max
arr = np.array(df) #
import matplotlib.pyplot as plt  # 可视化绘制
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
x = range(100)
plt.plot(x,arr[:,0],color='g',linewidth=1,linestyle='--')
plt.xlabel('调整主要操作变量幅度值的轮次') #X轴标签
plt.ylabel("辛烷值") #Y轴标签
plt.title("辛烷值变化轨迹 ") #标题
plt.savefig('辛烷值变化轨迹.jpg',dpi = 900)
plt.figure()
x1= range(100)
plt.plot(x1,arr[:,1],color='red',linewidth=1,linestyle='--')
plt.xlabel('调整主要操作变量幅度值的轮次') #X轴标签
plt.ylabel("硫含量 ug/g") #Y轴标签
plt.title("硫含量变化轨迹ug/g") #标题
plt.savefig('硫含量变化轨迹.jpg',dpi = 900)

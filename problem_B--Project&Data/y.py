# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 03:53:23 2020

@author: 11854
"""
import numpy as np
import pandas as pd
df = pd.read_csv("y.csv",header = None) #读取训练集csv文件,新的y_max
arr = np.array(df) #
df1 = pd.read_csv("predicted_y.csv",header = None) #读取训练集csv文件,新的y_max
arr1 = np.array(df1) #
import matplotlib.pyplot as plt  # 可视化绘制
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
x = range(325)
plt.plot(x,arr,color='g',linewidth=1,linestyle='--')
plt.plot(x,arr1,color='r',linewidth=1,linestyle='--')
plt.xlabel('样本编号') #X轴标签
plt.ylabel("辛烷值") #Y轴标签
plt.title("辛烷值预测对比图 ") #标题

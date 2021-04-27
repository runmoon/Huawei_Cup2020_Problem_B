# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:18:30 2020

@author: 11854
"""
import numpy as np
import pandas as pd
import warnings
import datetime
start = datetime.datetime.now()
warnings.filterwarnings("ignore")
#import matplotlib.pyplot as plt
#df = pd.read_csv("1.csv",header = None) #读取csv文件
df = pd.read_csv("285data.csv",header = None) #读取285csv文件
df1 = pd.read_csv("313data.csv",header = None) #读取313csv文件 
arr285 = np.array(df) #使用numpy转化为矩阵格式
arr313 = np.array(df1) #使用numpy转化为矩阵格式

mean285 = arr285.mean(axis=0) #均值
std285 = arr285.std(axis=0) #标准差
range_low285 = mean285-3*std285 #下限
range_high285 = mean285+3*std285 #上限
num = 0
num1 = 0
mean313 = arr313.mean(axis=0)
std313 = arr313.std(axis=0)
range_low313 = mean313-3*std313
range_high313 = mean313+3*std313
new_data285 = arr285
new_data313 = arr313
new_data313 = pd.DataFrame(new_data313)
# for i in range(40):  #行
#   for j in range(354):  #属性
#      if range_low285[j] > arr285[i,j] or arr285[i,j] > range_high285[j]:
#          print('i',i)
#          new_data285 = new_data285.drop([i],axis=0)
#          num = num+1
#          print('num:',num)
#          break
# data285 = new_data285
row313 = []  
for i in range(40):  #行
  for j in range(354):  #属性
     if range_low313[j] > arr313[i,j] or arr313[i,j] > range_high313[j]:
         print('i',i)
         print('j',j)
         # new_data313 = new_data313.drop([i,j],axis=0)
         # num1 = num1+1
         # print('num:',num1)
         break
# data313 = new_data313
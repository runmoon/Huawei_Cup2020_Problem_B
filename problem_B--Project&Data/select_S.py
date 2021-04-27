# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:44:11 2020

@author: 11854
"""
import numpy as np
import pandas as pd
df = pd.read_csv("S_y.csv",header = None) #读取训练集csv文件,新的A
arr = np.array(df) #针对训练集A，使用numpy转化为矩阵格式
df1 = pd.read_excel("data.xlsx",header = None) #读取训练集csv文件,新的A
arr1 = np.array(df1) #针对训练集A，使用numpy转化为矩阵格式
df2 = pd.read_csv("y_max.csv",header = None) #读取训练集csv文件,新的y_max
arr2 = np.array(df2) #
df3= pd.read_csv("y.csv",header = None) #读取训练集csv文件,新的y_max
arr3 = np.array(df3) #真实的y

save = []
S = np.zeros([1,27])
y_max = np.zeros([1,1])
y_real = np.zeros([1,1])
for i in range(325):
    if(arr[i]<=5.0):
        save.append(i)
        S = np.insert(S,0,values = arr1[i,:],axis = 0)
        y_max = np.insert(y_max,0,values = arr2[i,:],axis = 0)
        y_real = np.insert(y_real,0,values = arr3[i,:],axis = 0)
S1 = np.zeros([1,27]) #S1为筛选后的样本
y_max1 = np.zeros([1,1])
y_real1 = np.zeros([1,1])
for i in range(268):
    S1 = np.insert(S1,0,values = S[i,:],axis = 0)
    y_max1 = np.insert(y_max1,0,values = y_max[i,:],axis = 0)
    y_real1 = np.insert(y_real1,0,values = y_real[i,:],axis = 0)
S1 = np.delete(S1,268,axis = 0) #S1为筛选后的样本
y_max = np.delete(y_max1,268,axis = 0) #S1为筛选后的样本
y_real = np.delete(y_real1,268,axis = 0) #S1为筛选后的样本
np.savetxt("selected_data.csv", S1, delimiter=',') 
np.savetxt("selectedy_max.csv", y_max, delimiter=',')
np.savetxt("selectedy_real.csv", y_real, delimiter=',')     
    
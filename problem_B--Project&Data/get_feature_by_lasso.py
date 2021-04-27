# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:39:06 2020

@author: 11854
"""
import time
import pandas as pd
import numpy as np
from sklearn.linear_model import LassoCV, LassoLarsCV, LassoLarsIC
# from sklearn.linear_model import Ridge, RidgeCV   # Ridge岭回归,RidgeCV带有广义交叉验证的岭回归
import matplotlib.pyplot as plt  # 可视化绘制
#import matplotlib as mpl
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# mpl.rcParams.update(
# {
# 'text.usetex': False,
# 'font.family': 'stixgeneral',
# 'mathtext.fontset': 'stix' ,
# }
# )
# from pylab import *
# mpl.rcParams['font.sans-serif']=['SimHei']
X = pd.read_excel("data.xlsx",header = None) #读取csv文件
#X = pd.read_csv("select.csv",header = None) #读取csv文件
y = pd.read_csv("y.csv",header = None) #读取csv文件
# 生成X和y矩阵 
X = np.array(X)
y = np.array(y)

########lasso###########
from sklearn import linear_model
#reg = linear_model.Lasso(alpha = 0.001)#辛烷的alpha
reg = linear_model.Lasso(alpha = 0.002)#S的alpha
reg.fit(X,y) #X是所有特征
W = reg.coef_
W = np.array(W)
w0 = reg.intercept_
print('w0 = ',w0)
#np.savetxt("W.csv", W, delimiter=',')
np.savetxt("S_W.csv", W, delimiter=',')
sum = 0
EPSILON = 1e-4
for i in range(27):
    if(W[i]==0):
        sum = sum+1
        print(i)
    # if(W[i]!=0):
    #     print(i)
#print(reg.coef_)
print("------0的个数-----",sum)
predicted = reg.predict(X)
predicted = np.array(predicted)
np.savetxt("predicted_y.csv", predicted, delimiter=',')
model_bic = LassoLarsIC(criterion='bic')
t1 = time.time()
model_bic.fit(X, y)
t_bic = time.time() - t1
alpha_bic_ = model_bic.alpha_

model_aic = LassoLarsIC(criterion='aic')
model_aic.fit(X, y)
alpha_aic_ = model_aic.alpha_

def plot_ic_criterion(model, name, color):
    criterion_ = model.criterion_
    plt.semilogx(model.alphas_ + EPSILON, criterion_, '--', color=color,
                  linewidth=3, label='%s criterion' % name)
    plt.axvline(model.alpha_ + EPSILON, color=color, linewidth=3,
                label='alpha: %s estimate' % name)
    plt.xlabel(r'$\alpha$')
    plt.ylabel('criterion')


plt.figure()
# plot_ic_criterion(model_aic, 'AIC', 'b')
plot_ic_criterion(model_bic, 'AIC', 'r') 
plt.legend()
plt.title('Information-criterion for model selection (training time %.3fs)'
          % t_bic)
plt.savefig('alpha.jpg',dpi = 900)
from sklearn.metrics import mean_squared_error #均方差
from sklearn.metrics import mean_absolute_error #平方绝对误差
from sklearn.metrics import r2_score#R square  R_square一般用于回归中评估模型的好坏程度，其值越接近1，代表模型性能越好
#调用
mse = mean_squared_error(y,predicted)
mae = mean_absolute_error(y,predicted)
r2 = r2_score(y,predicted)
print('r2 = ',r2)
print('mse = ',mse)
print('mae = ',mae)
plt.figure()
x = range(325)
plt.plot(x,y,color='g',linewidth=1,linestyle='--')
plt.plot(x,predicted,color='red',linewidth=1,linestyle='--')
plt.xlabel('样本编号') #X轴标签
plt.ylabel("辛烷值") #Y轴标签
plt.title("辛烷值预测对比图") #标题
plt.savefig('y.jpg',dpi = 900)


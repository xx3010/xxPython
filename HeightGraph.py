
# coding: utf-8

# In[11]:


#coding=utf-8
import scipy.stats as stats
from IPython.core.pylabtools import figsize
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

figsize(15, 10)

def height(x,y):
    return (20-x**2-y**3)
x=np.linspace(-3,3,20)
y=np.linspace(-3,3,20)
X,Y=np.meshgrid(x,y)
plt.contourf(X,Y,height(X,Y),20,alpha=0.75,cmap=plt.cm.rainbow)
#为等高线填充颜色 10表示按照高度分成10层 alpha表示透明度 cmap表示渐变标准
C=plt.contour(X,Y,height(X,Y),10,colors='black')
#使用contour绘制等高线
plt.clabel(C,inline=True,fontsize=10)
#在等高线处添加数字
plt.xticks(())
plt.yticks(())
#去掉坐标轴刻度
plt.show()
#显示图片


fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(X, Y, height(X,Y), cmap=plt.cm.coolwarm)
ax.view_init(30,30)


# In[85]:


import openpyxl
wb =openpyxl.load_workbook('Consolidation_20180925_5_2016.xlsm')
sheet = wb.get_sheet_by_name('EQ Vega')

def get_value_list(t_2d):
    return([[cell.value for cell in row] for row in t_2d])

data = get_value_list(sheet['C30:Y48'])
strike = get_value_list(sheet['C29:Y29'])
maturity = get_value_list(sheet['A30:A48'])

print(data)
print(strike)
print(maturity)


# In[ ]:


import openpyxl
wb =openpyxl.load_workbook('Consolidation_20180925_5_2016.xlsm')
sheet = wb.get_sheet_by_name('EQ Vega')

def get_value_list(t_2d):
    return([[cell.value for cell in row] for row in t_2d])

data = get_value_list(sheet['C30:Y48'])
strike = get_value_list(sheet['C29:Y29'])
maturity = get_value_list(sheet['A30:A48'])

print(data)
print(strike)
print(maturity)


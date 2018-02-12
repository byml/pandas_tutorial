# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ppv3 = pd.DataFrame()

plt.figure(figsize=(10,6))
#设置x轴柱子的个数
x=np.arange(14)+1 #课程品类数量已知为14，也可以用len(ppv3.index)
#设置y轴的数值，需将numbers列的数据先转化为数列，再转化为矩阵格式
y=np.array(list(ppv3['numbers']))
xticks1=list(ppv3.index) #构造不同课程类目的数列
#画出柱状图
plt.bar(x,y,width = 0.35,align='center',color = 'c',alpha=0.8)
#设置x轴的刻度，将构建的xticks代入，同时由于课程类目文字较多，在一块会比较拥挤和重叠，因此设置字体和对齐方式
plt.xticks(x,xticks1,size='small',rotation=30)
#x、y轴标签与图形标题
plt.xlabel('课程主题类别')
plt.ylabel('number')
plt.title('不同课程类别的平均学习人数')

#设置y轴的范围
plt.ylim(0,3700)
plt.show()


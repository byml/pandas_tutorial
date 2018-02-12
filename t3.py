# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

people = ('James', 'Durant', 'Kobe', 'Wade', 'Curry','Magic','Hardan')
y_pos = np.arange(len(people))
performance = 30 + 70 * np.random.rand(len(people)) #随机产生len(people)个 [0,1）的数
error = np.random.rand(len(people))
plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)#这里是产生横向柱状图 barh h--horizontal
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.xlim(0,100)
plt.title('How efficient do you want to go today?')
for i in range(0, len(people)):
    plt.text(performance[i], i, performance[i].round(2), color = 'red')

#

plt.savefig('1.jpg')
plt.show()
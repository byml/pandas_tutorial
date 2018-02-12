# -*- coding: utf-8 -*-


from numpy.random import randn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(abs(randn(10,5)),columns=['A','B','C','D','E'],index = np.arange(0,100,10))
df.plot(kind='bar', figsize=(10,8))
print(df)
plt.show()

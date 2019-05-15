import tushare as ts
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt

# 获取数据
df = ts.get_hist_data('600702',start='2019-01-01',end='2019-05-15')
df = df.sort_index(axis=0,ascending=True)

# 分析数据
print(df.corr())
scatter_matrix(df,figsize=(12,12))

plt.show()
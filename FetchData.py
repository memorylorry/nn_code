import tushare as ts
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt

# 获取数据
df = ts.get_hist_data('600702',start='2019-11-01',end='2020-04-04')

df = df.drop(['p_change','ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20'],axis=1)

print(df.columns)
df.to_csv('data.csv')
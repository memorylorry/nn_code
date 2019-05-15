import pandas as pd
import numpy as np

# 创建序列
s1 = pd.Series([1,3,4])
print(s1)

s2 = pd.Series(np.arange(5))
print(s2)

# 创建dataFrame
df1 = pd.date_range('20151203',periods=6)
print(df1)

df2 = pd.DataFrame({
    'A':1,
    'B':2,
    'C':np.arange(3)
})
print(df2)

# 转换回numpy格式
print(df2.to_numpy())

# 按照索引排序
print(df2.sort_index(axis=1,ascending=False))
# 按照值排序
print(df2.sort_values(by='C',ascending=False))

df3 = pd.DataFrame({
    'Z':np.arange(10)%3,
    'A':np.random.random(10),
    'B':np.random.random(10)
})
print(df3.groupby('Z').sum())
import pandas as pd

# 读取无标题的csv
df:pd.DataFrame = pd.read_csv('data_without_title.csv',
                              sep=',',
                              header=None,
                              names=['date','open','high','close','low','volume','price_change'])

print(df.index)
print(df.columns)
print(df['open'])


# 读取有标题的csv
df2:pd.DataFrame=pd.read_csv(
                                filepath_or_buffer='data.csv',
                                sep=',',
                                header=0,    # 指定标题行
                                index_col=0,  # 指定索引列
                                usecols=[0,1,2] # 指定使用的列
                             )

print(df2.index)
print(df2.columns)
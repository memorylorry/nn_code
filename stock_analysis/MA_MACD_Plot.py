import pandas as pd
import numpy as np
import talib as tl
import tushare as ts
import matplotlib.pyplot as plt
import mplfinance as mpf

df=pd.read_csv('data.csv',index_col=0,parse_dates=['date'])


exp12 = df['close'].ewm(span=12, adjust=False).mean()
exp26 = df['close'].ewm(span=26, adjust=False).mean()
macd = exp12 - exp26
signal= macd.ewm(span=9, adjust=False).mean()
histogram:pd.Series = macd - signal
histogram_positive = np.maximum(histogram,0)
histogram_negative = np.minimum(histogram,0)
print(type(histogram_positive))

apds = [
    mpf.make_addplot(histogram_positive,type='bar',width=0.7,panel=1,color='#ff0000',alpha=1,secondary_y=False),
    mpf.make_addplot(histogram_negative,type='bar',width=0.7,panel=1,color='#00ff00',alpha=1,secondary_y=False),
    mpf.make_addplot(macd,panel=1,color='#FFFF00',secondary_y=True),
    mpf.make_addplot(signal,panel=1,color='#FF33CC',secondary_y=True)
]

mpf.plot(df,type='candle',style='yahoo',volume=True,volume_panel=2,addplot=apds)


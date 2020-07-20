import numpy as np
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
import mplfinance as mpf

ts.set_token('538454b8b51bdde143443904afd9043337fcd4b94a264b74d0c5b196')
pro = ts.pro_api()



'''
FilterMethod 用于设计过滤方法，是整个过滤方法的基类
'''
class FilterMethod:
    def filter(self,price, *args, **kwargs):
        '''
            根据filter返回的布尔值，上层会据此来筛选数据
            @return type - bool
        '''
        return True
class FilterMethod2:
    def filter(self,price, *args, **kwargs):
        '''
            根据filter返回的布尔值，上层会据此来筛选数据
            @return type - bool
        '''
        return price>3


class Filter:
    def filter_list(self,stock_list:np.ndarray,filter_method=FilterMethod(),*args, **kwargs):
        '''
            根据输入的数据筛选n条数据
            @return type - bool
        '''
        idx= []
        for one in stock_list:
            idx.append(self.filter(one,filter_method=filter_method,args=args,kwargs=kwargs))
        return stock_list[idx]

    def filter(self,stock_list,filter_method=FilterMethod(), *args, **kwargs):
        '''
            根据输入的数据筛选1条数据
        '''
        price=stock_list
        ans = filter_method.filter(price, args, kwargs)
        return ans


# list=np.array([1,2,3,4,5,6])
# f=Filter()
# z=f.filter_list(list,filter_method=FilterMethod2())
# print(z)

# print(list[list>3])

df = ts.pro_bar(ts_code='000001.SZ', start_date='20200501', end_date='20207011',freq='60min')
with open('zzz.csv','w+') as fw:
    fw.write(df.to_csv())

#
# df:pd.DataFrame = pd.read_csv('zzz.csv',parse_dates=['datetime'],index_col=2)[::-1]
# df.rename(columns={'vol':'volume'}, inplace=True)

# MACD
# exp12 = df['close'].ewm(span=12, adjust=False).mean()
# exp26 = df['close'].ewm(span=26, adjust=False).mean()
# macd = exp12 - exp26
# signal= macd.ewm(span=9, adjust=False).mean()
# histogram:pd.Series = macd - signal
# histogram_positive = np.maximum(histogram,0)
# histogram_negative = np.minimum(histogram,0)


print(df)
#
# apds = [
#     mpf.make_addplot(histogram_positive,type='bar',width=0.7,panel=1,color='#ff0000',alpha=1,secondary_y=False),
#     mpf.make_addplot(histogram_negative,type='bar',width=0.7,panel=1,color='#00ff00',alpha=1,secondary_y=False),
#     mpf.make_addplot(macd,panel=1,color='#FFFF00',secondary_y=True),
#     mpf.make_addplot(signal,panel=1,color='#FF33CC',secondary_y=True)
# ]
#
# mpf.plot(df,style='yahoo',type='candle',addplot=apds,volume=True,volume_panel=2)
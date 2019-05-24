import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix

df = pd.read_csv('./housing.csv')

# 查看地理位置的密集度
#plt.plot(df['longitude'],df['latitude'],'rp',alpha=0.2)
#plt.show()

'''
# 查看指标间的相互关系
The correlation coefficient ranges from –1 to 1. When it is close to 1, it means that
there is a strong positive correlation; for example, the median house value tends to go
up when the median income goes up. When the coefficient is close to –1, it means
that there is a strong negative correlation;
'''
#print(df.corr())
#scatter_matrix(df,figsize=(22,22))
#plt.show()


'''
# 计算新的指标，使得新指标比原有指标相关度更高
'''
df['rooms_per_household'] = df['total_rooms']/df['households']
df['bedrooms_per_room'] = df['total_bedrooms']/df['total_rooms']

cor = df.corr()
print(cor['median_house_value'].sort_values(ascending=False))


'''
let’s separate the predictors and the labels since we don’t necessarily want to apply
the same transformations to the predictors and the target values (note that drop()
creates a copy of the data and does not affect strat_train_set )

'''






ho = df.drop('median_house_value',axis=1)
print(ho.columns)

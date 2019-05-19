import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('cost.csv')

plt.plot(df['date'],df['all_assets'],'rx')
plt.plot(df['date'],df['all_debit'],'bx')
plt.show()
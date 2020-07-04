import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

open = np.loadtxt('data.csv',skiprows=1,delimiter=',',usecols=(1))
open = open[::-1] # 逆序

value = np.ones(5)*100
inc = np.arange(0,5)
inc = 1.05**inc
df = np.convolve(value,inc)
print(df)


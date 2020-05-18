import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

arr = np.arange(12).reshape(3,4)
print(arr)
r1 = arr.min(axis=0)
r2 = arr.min(axis=1)
print(r1)
print(r2)


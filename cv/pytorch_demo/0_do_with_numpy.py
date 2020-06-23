import numpy as np
import matplotlib.pyplot as plt

# prepare data
data = np.loadtxt('house.csv',delimiter=' ')
x_r:np.ndarray = data[:,0]
y:np.ndarray = data[:,3]


# parameter
theta:np.ndarray = np.array([[0,0]],dtype=np.float)
x = np.column_stack((np.ones(x_r.size),x_r))
alpha = 0.000000003
list = []
k1 = []
k2 = []

plt.figure(figsize=(10,10))

for i in range(5000):
    # 计算偏导
    y_p:np.ndarray = x.dot(theta.T).flatten()
    y_dif = y_p - y
    delta_w = np.sum(y_dif * x_r) / x.size
    delta_b = np.sum(y_dif) / x.size
    # 计算损失度
    loss = np.square(y_p - y).sum() / x.size
    list.append(loss)
    print(loss)
    # 更新theta
    theta[0][0] -= alpha * delta_b
    theta[0][1] -= alpha * delta_w
    k1.append(theta[0][0])
    k2.append(theta[0][1])

plt.subplot(3,1,1)
plt.plot(list,'rx',alpha=0.03)
plt.subplot(3,1,2)
plt.plot(x_r,y,'rx')
plt.plot(x_r,y_p,'k-')
plt.subplot(3,1,3)
plt.plot(k1,k2,'k-')

plt.show()
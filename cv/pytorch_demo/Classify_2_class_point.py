import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F

# 产生数据
n_data = torch.ones(100,2)
x1 = torch.normal(n_data*2,1)
y1 = torch.zeros(100)
x2 = torch.normal(n_data*4,1)
y2 = torch.ones(100)

x = torch.cat((x1,x2),0).type(torch.float)
y =torch.cat((y1,y2)).type(torch.long)

# 绘图
plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.title("raw data")
plt.plot(x1[:,0],x1[:,1],'yo',alpha=0.5)
plt.plot(x2[:,0],x2[:,1],'ro',alpha=0.5)

# 定义模型
model = torch.nn.Sequential(
    torch.nn.Linear(2,100),
    torch.nn.ReLU(),
    torch.nn.Linear(100,2)
)

# 定义优化器、损失函数
optimizer = torch.optim.SGD(model.parameters(),lr=1e-3)
loss_fn = torch.nn.CrossEntropyLoss()

# 训练模型
for i in range(3000):
    output = model(x)
    loss = loss_fn(output,y)
    # if i%50 == 0:
    #     print(loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


# 绘制预测图
_, predicted = torch.max(output, 1)
c1 = x[predicted==0]
c2 = x[predicted==1]
plt.subplot(1,2,2)
plt.title("train model")
plt.plot(c1[:,0],c1[:,1],'yo',alpha=0.5)
plt.plot(c2[:,0],c2[:,1],'ro',alpha=0.5)
plt.show()


# 模型评估的指标
t = predicted[predicted==0]
f = predicted[predicted==1]
tp_pos = (t - y[predicted==0]) == 0
fn_pos = (t - y[predicted==0]) != 0
tn_pos = (f - y[predicted==1]) == 0
fp_pos = (f - y[predicted==1]) != 0

tp = len(t[tp_pos])
fn = len(t[fn_pos])
tn = len(f[tn_pos])
fp = len(f[fp_pos])

# 准确率(Accuracy):模型判断正确的数据(TP+TN)占总数据的比例
print('accuracy is : ',(tp+tn)/200)
# 召回率(Recall): 针对数据集中的所有正例(TP+FN)而言,模型正确判断出的正例(TP)占数据集中所有正例的比例
print('recall rate is : ',tp/(tp+fn))
# 精确率(Precision):针对模型判断出的所有正例(TP+FP)而言,其中真正例(TP)占的比例.
print('precision is : ',tp/(tp+fp))

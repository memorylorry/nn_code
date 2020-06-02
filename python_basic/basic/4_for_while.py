# For
for i in range(0,3):
    print('range - '+str(i))

# While
i = 0
while i<10:
    if i == 6:
        break            # use break 提前跳出循环
    if i%2 != 0 :
        i = i + 1
        continue         # 用 continue 提前进入下一个循环阶段
    print('reach this scope! - ' + str(i))
    i = i + 1

# While-Else
i = 0
while i < 3:
    i = i + 1
else:
    print('While-Else End')
x = input('Input X:')
y = input('Input Y:')
if x.isdigit() and y.isdigit():
    print(int(x)+int(y))
else:
    print('x is ' + x + ' and y is ' + y)

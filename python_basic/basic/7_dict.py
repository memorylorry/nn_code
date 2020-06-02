user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

user_0['new'] = 'test'
del user_0['new']

# 遍历dict
for key,value in user_0.items():
    print(key + ' : '+value)
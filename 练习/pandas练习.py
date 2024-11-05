import pandas as pd

a = [1, 2, 3]
b = [4, 5, 6]

# 不指定索引自动从0开始
myvar = pd.Series(b)
print(myvar)
# for i in myvar:
#     print(i)
print(myvar[2])
print('********************************************************************')

# 2. 指定索引
str1 = ['google', 'facebook', 'github']
mystr = pd.Series(str1, index=["x", "y", "z"])
print(mystr)
print(mystr['x'])
print(mystr['y'])
print('********************************************************************')

# 3. key/value 对象， 类似字典来创建Series
sites = {1: 'google', 2: 'tencent', 3: 'weiwei'}
mysites = pd.Series(sites, name="dahezhiquan")
mysites = pd.Series(sites,  name="dahezhiquan")
print(mysites)
print(mysites.name)  # name属性指的是这个series的名字





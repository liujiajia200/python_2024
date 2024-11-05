# 1. 不可变数据类型
#     数字类型 int bool float complex long
#     字符串 str
#     元组 tuple
# 2. 可变数据类型
#     列表 list
#     字典 dict

# 1. 不可变数据类型举例，当给变量重新赋值后，变量的id变化了，说明其为不可变数据类型
print('--------------------------不可变数据类型--------------------------')
a = 1  # int
print(id(a))

a = 0.5  # float
print(id(a))

a = 'a'  # str
print(id(a))

a = True
print(id(a))

a = (1, 2, 3)  # 元组
print(id(a))

print('--------------------------可变数据类型--------------------------')
# 2. 可变数据类型举例，当给变量重新赋值后，变量的id没变化，说明其为可变数据类型

# (1) 字典
print('-------------字典------------')

dic_a = {1: "nihao", 2: "hha"}
print(id(dic_a))
dic_a.pop(1)
print(dic_a)
print(id(dic_a))

dic_a[3] = "wowowo"
print(dic_a)
print(id(dic_a))

print('-------------列表------------')
# (3) 列表
list_1 = [1, 2, 3]
print(id(list_1))

list_1.append(4)
print(list_1)
print(id(list_1))



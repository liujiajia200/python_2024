#  1. 字典是无序的对象结合， 列表是有序的对象集合
#  2. 键必须是唯一的，
#  3. 值可以取任何数据类型，但是键只能使用字符串，数字或元组

xiaoming = {
    "name": 'xiaoming',
    "age": 18,
    "gender": True,
    "height": 1.75
}
keys = xiaoming.keys()  # 1. keys() 所有的key
print(type(keys))
print(keys)
print('^^^^^^^^^^^^^^^^')
values = xiaoming.values()  # 2. values() 所有的values
print(type(values))
print(values)

print(xiaoming.items())  # 3. items（）所有的项

# 4. 取值
print(xiaoming["name"])

# 5. 修改值或增加值
xiaoming["name"] = '张三'  # 修改xiaoming name值
print(xiaoming)

xiaoming['chengji'] = 90  # 增加值
print(xiaoming)

#  6. 统计字典中数据个数
print(len(xiaoming))

# 7. 合并字典
temple_dic = {"height": 175,
              "age": 20}

xiaoming.update(temple_dic)  # update: 合并字典， 如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
print(xiaoming)

new_dic = {"year": 1995, "month": 12}
xiaoming.update(new_dic)
print(xiaoming)

#  8. 清空字典

# xiaoming.clear()
# print(xiaoming)

#  9. 遍历字典， 在开发工作中由于字典中存储的数据是不同类型的，所以遍历的需求并不多
for k in xiaoming:
    print("%s: %s" % (k, xiaoming[k]))   # 简单方式遍历

for k in xiaoming.keys():  # 复杂方式遍历， 不需要记住
    print(xiaoming[k])


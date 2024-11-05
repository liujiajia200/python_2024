# string 列表 元组  元组 都是非数字型的数据类型， 所以有以下共同点

# 1. 都是一个序列 sequence，也可以理解为容器
# 2. 取值[]
# 3. 遍历 for in
# 4. 计算长度、最大/最小值、 比较 、 删除
# 5. 链接+ 和重复 *
# 6. 切片



# 通常列表种的数据类型一致，虽然它可以存储不同类型的元素
name_list = ['zhangsan', 'lisi', 'wangwu']
temp_list = ['孙悟空', '沙师弟', '猪八戒']

name_list.insert(1, 'goudan')  # 1. insert
name_list.extend(temp_list)  # 2. extend: extend一个新的列表
name_list.remove('猪八戒')  # 3. remove
name_list.append('白骨精')  # 4. append： 在末尾追加
name_list.pop()  # 5. 默认删除最后一个元素，
name_list.pop(3)  # 6. 如果加了索引就删除指定元素
print(f'name_list的长度是{len(name_list)}') # 7. 计算列表元素数量（长度）
print(name_list)


name_list.append('haha')
name_list.extend('good')
print('------------------------')
print(name_list)
print(name_list.count('good'))  # 'good' 在name_list出现的次数
print(name_list.count('zhangsan'))
print('**********************')
num_list = [4, 3, 9, 5, 0]
num_list.sort()  # 8. 排序
name_list.sort()  # 9. 按照字母顺序排序
name_list.sort(reverse=True)  # 9. 按照字母顺序排序 （降序）

print(num_list)
print(name_list)
print('&&&&&&&&&&&&&&&&&&&&&&&&')

new_list = ['a', 'd', 'b', 'f']  # 10. 反转
new_list.reverse()
print(new_list)

print('^^^^^^^^^^^^^^^^^')
for a in name_list:
    if a == 'b':
        print(a)
else:
    print(f'name_list中没有字母b')

d=[0,1,2,3,4,5,6,7,8,9,10]
print(d[0:11:2])
print(d[1:11:3])





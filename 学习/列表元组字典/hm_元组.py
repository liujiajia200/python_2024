#  1. 元组中的元素不能修改
#  2. 在开发中很少用for in 遍历元组tuple
#  3. 通常用tuple作为函数的参数和返回值


#  空元组
tuple_a = ()
info_tuple = ('zhangsan', 17, 1.75, 'zhangsan')

# 只有一个元素的元组
one_tuple = 'lisi',

print(type(one_tuple))
print(info_tuple.index(17))  # 1. index
print(info_tuple.index('zhangsan'))  # 2. index: 只显示第一个'zhangsan'出现的位置
print(info_tuple.count('zhangsan'))  # 3. count: 计算元祖中出现'zhangsan'出现的次数
print(len(info_tuple))  # len: 计算元组长度

# 元组和列表相互转化
tuple_a = ('lisi', 18, 'ping')
list_q = ['a', 'b', 'd', 'c']

new_list = list(tuple_a)
print(type(new_list))

new_tuple = tuple(list_q)
print(type(new_tuple))

# 格式字符串
info_tuple1= ('liugouzi', 17, '男')
print('%s今年%d岁了，他是个%s的' % info_tuple1)




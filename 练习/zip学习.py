# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [4, 5, 6, 7, 8]
# zipped = zip(a, b)  # 返回一个对象
# print(list(zipped))


# list(zipped)  # list() 转换为列表
# [(1, 4), (2, 5), (3, 6)]
# list(zip(a, c))  # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
#
# a1, a2 = zip(*zip(a, b))  # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
# print(*zip(a, b))
# print(list(a1))
# print(list(a2))

# result = zip(a, b)
# a, b = zip(*result)
# print(a)
# print(b)


# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 “”。
#
# 示例 1:
#
# 输入: [“flower”,“flow”,“flight”]
# 输出: “fl”
# 示例 2:
#
# 输入: [“dog”,“racecar”,“car”]
# 输出: “”
# 解释: 输入不存在公共前缀。
# 说明: 所有输入只包含小写字母 a-z

# 遗憾： 没用到zip
def get_max_ex(str_list):
    shortest_ele = min(str_list, key=len)
    i = len(shortest_ele)
    while i > 0:
        re = [str1 for str1 in str_list if shortest_ele[0:i] in str1]
        if len(re) == 3:
            return shortest_ele[0:i]
        i -= 1


a = ['flower', 'flow', 'flight']
result = get_max_ex(a)
print(result)

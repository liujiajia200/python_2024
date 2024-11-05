import string

s1 = "abcdefg"
# 1. 统计字符串长度
print(len(s1))

# 2. 寻找'a' 和 'fg' 在字符串中第一次出现的位置
print(s1.index('a'))
print(s1.index('fg'))

# 3. 取字符串中索引为2的值
print(s1[2])

# 4. 计算'ab'在字符串中出现的次数
print(s1.count('ab'))

print('*'*50)

# 5. 判断字符串是否包含空格
is_contains_space = s1.isspace()
print(is_contains_space)
s2 = " "
is_contains_space = s2.isspace()
print(is_contains_space)

s2_2 = "    \t\n\r"
print(f's2_2中是否包含空格：{s2_2.isspace()}')

# 6. 判断字符串是否为空
s3 = None
s3 = ""   # 不是none
if s3 is None:
    print('s3 是none')
else:
    print("s3 不是 none")

print("$"*50)
# 7. 大小写转换
s4 = "hello word"

# (1) 把字符串中的第一个字符大写
s4 = s4.capitalize()
print(s4)

# (2) 把字符串的每个单词首字母大写
s4 = "hello word"
s4 = s4.title()
print(s4)

# (3) 把string 中所有的大写字母为小写  ------奇怪 不管用
s5 = "Hi"
s5 = s5.lower()
print(s5)

# (4) 把string 中所有的小写字母为大写
s7 = 'hello word'
s7 = s7.upper()
print(s7)

# (5) 反转string中的大小写
s8 = 'hJ FFd'
s8 = s8.swapcase()
print(s8)


print('&'*50)
# 8. 查找和替换 startwith endwith find
s9 = 'hello Word'
print(s9.startswith('h'))
print(s9.endswith('Word'))
# find: 检查str是否包含在string中，如果start和end指定范围，则检查是否版旱灾指定范围内，如果返回开始的索引值，否则返回-1
print(s9.find('llo', 0, 5))
print(s9.find('llo'))
print(s9.find('ooo'))

print('!'*50)
# replace
s10 = "hello word"
s10 = s10.replace('hello', 'hi')
print(s10)







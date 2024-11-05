# 1. 给定一个整数数组 nums和一个整数目标值target， 请你在该数组中找出和为目标值target的那两个整数， 并返回他们的数组下标。
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 10
#
# i = 0
# while i < len(nums):
#     j = i + 1
#     while j < len(nums):
#         if nums[i] + nums[j] == target:
#             print(f"{target} = nums[{i}]({nums[i]}) + nums[{j}]({nums[j]})")
#         j = j + 1
#     i = i + 1
#
#
# def lian_xu():
#     """ lianxi """
#
#     print("lianxi")
import random

from pip._internal.utils.misc import enum


# citys = 'shanghai'
#
# for i, text in enumerate(citys):
#     print(i, text)
#
# citys = ('shanghai', 'chegnde')
# for i in enumerate(citys):
#     print(i)
#
# for i in list(enumerate(citys)):
#     print(i)
#
# citys = {'jiajia': 19,
#          'linlin': 20}
#
# for i in list(enumerate(citys.keys())):
#     print(i)
#
# for i in list(enumerate(citys.values())):
#     print(i)
#
# for i in range(4):
#     if i == 2:
#         break
#     print(i)
# else:
#     print('jajjaj')
# print('--------------------------------------')
# i = 0
# while i < 4:
#     i = i + 1
#     if i == 1:
#         continue
#     if i == 3:
#         break
#     print(i)
#
#
# else:
#     print('kkkkkk')
#
#
# print('00000000000000000000000000000000000000000')
# for i in range(5):
#     if i == 2:
#         continue
#     if i == 3:
#         break
#     print(i)
#
# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# a = random.choice([0, 1])
# a = random.choice([0, 1, 2, 3])
# b = range(3)
# for i in b:
#     print(i)
# print(a)
# print(b)
# print(c)

# documents = ['self.letter_radio_button', 'self.student_id_card_radio_button']
# a = range(0, len(documents))
# print(a)
# print(random.choice(a))


# dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}


# for key in dic:
#     print(dic[key])

# for i in dic.keys():
#     print(i)
#
# for value in dic.values():
#     print(value)
#
# a = list(dic.items())
# print(a)
# print(type(a))
# print(a[0])
#
# del(dic['lilei'])
# print(dic)

# f = open('/Users/jiajliu/desktop/text.txt', 'r')
# lines = f.readlines()
# print(lines)
# f.close()
#
# f = open('/Users/jiajliu/desktop/text.txt', 'w')
# f.write('abc')
# f.close()

# def func(*dict):
#     print(type(dict))
#     print(dict)
#
#
# func(1, 9)
# func(2, 1, 11)
#
#
# def func(**dict):
#     print(type(dict))
#     print(dict)
#
#
# func(a=1, b=9)
# func(m=2, n=1, c=11)


# S = 'abcdefghijk'
# for (index, char) in enumerate(S):
#     print(index)
#     print(char)
#
# for index, char in enumerate(S):
#     print(index)
#     print(char)

# ta = [1, 2, 3]
# tb = [9, 8, 7]
# tc = ['a', 'b', 'c']
# for (a, b, c) in zip(ta, tb, tc):
#     print(a, b, c)

# ta = [1, 2, 3]
# tb = [9, 8, 7]
#
# # cluster
# zipped = zip(ta, tb)
# print(zipped)
#
# # decompose
# na, nb = zip(*zipped)
# print(na, nb)

# 生成器
# def gen():
#     a = 100
#     yield a
#     a = a * 8
#     yield a
#     yield 1000
#
#
# for i in gen():
#     print(i)

# 表推到，快速制表
# L = [i ** 2 for i in range(10)]
# print(L)
#
# xl = [1, 3, 5]
# yl = [9, 12, 13]
# L = [x ** 2 for (x, y) in zip(xl, yl) if y > 10]
# print(L)

# map()
# re = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
# print(list(re))

# map函数的第一个参数，可以是一个方法，这个方法不一定非得是lamda表达式
# def fuc(x, y):
#     return x + y
#
#
# re = map(fuc, [1, 2, 3], [1, 2, 3])
# print(list(re))

# filter 就算结果为true的元素存储到表中返回
# def func(a):
#     if a > 100:
#         return True
#     else:
#         return False
#
#
# print(list(filter(func, [10, 56, 101, 500])))

# re = iter(range(5))
# print(next(re))

# def generate_numbers():
#     num = 0
#     while True:
#         yield num
#         num += 1


# numbers_iter = generate_numbers()
# for _ in range(5):
#     print(next(numbers_iter))

# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         result = self.data[self.index]
#         self.index += 1
#         return result
#
#
# numbers = [1, 2, 3, 4, 5]
# my_iter = MyIterator(numbers)
# for num in my_iter:
#     print(num)

# def create_numbers(n):
#     for i in range(n):
#         yield i
#
#
# nums = create_numbers(5)
# for num in nums:
#     print(num)

# def test():
#     f = [1, 2]
#     sum = 0
#     try:
#         for i in f:
#             sum += int(i)
#             return sum
#     except Exception:
#         pass
#     finally:
#         sum = 10
#         print(sum)
#
#
# print(test())

# for i in range(3):
#     # if i > 1:
#     print('ddd')
# else:
#     print('lalalala')

# i = 3
# while i > 4:
#     print('jijiji')
#     i = i - 1
# else:
#     print('jujuju')

# class SampleMore(object):
#     def __call__(self, a):
#         return a + 5

# add = SampleMore()     # A function object
# print(add(2))          # Call function
# map(add, [2, 4, 5])


# token_err = {
#     'invalid': 'eyJraWQiOiJZNWh1MDNMZlp0NHZ4bWFhbEhtNXQxM0xkaHVxYVVxaEpsRGxrRTNwdFRrIiwiYWxnIjoiUlMyNTYifQ',
#     'expired': 'eyJraWQiOiJZNWh1MDNMZlp0NHZ4bWFhbEhtNXQxM0xkaHVxYVVxaEpsRGxrRTNwdFRrIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULkxSMlBoMDZaMzhLeTl6OUktM25YanpJd0xjM294UmNDUU9aTDB5TWNKVjgiLCJpc3MiOiJodHRwczovL2V3YmFuay5va3RhcHJldmlldy5jb20vb2F1dGgyL2F1c255Z3lteG52RTJodU9kMGg3IiwiYXVkIjoiaHR0cHM6Ly9kZXZhcGkuZWFzdHdlc3RiYW5rLmNvbSIsImlhdCI6MTcxNzU1NTgyNCwiZXhwIjoxNzE3NTU5NDI0LCJjaWQiOiIwb2EyMXF0a3l0dGJqMXlVYjBoOCIsInNjcCI6WyJhcGk6cmVhZCJdLCJzdWIiOiIwb2EyMXF0a3l0dGJqMXlVYjBoOCJ9.Me5gwN8YoVo7REJeMHHHcATC-aiALOzBrkkJabYg1lW0i54O8gocy0s4nfW6LNuyb7IX4eMRNtJY77rVjYKPGpxKivMh1QoUXo-hOutGKYqKtwvsNjXR2aP7u__bKvoB-bZEGRqUontdHylEE9qe797IwZTHWQDPppT8b2L9f9HexP2kyCG-HzE-OEZXyivRWlYoeGj9HALlPtSLvmRHvQVhHrdZ6kcBPZaKVFtPDfptt70cOy9pUyz1enihune5vGU90-kld0aqDokYmDEEyvZwpVEdwixbtsCJ2G6vpGOVhssbh0MDF6JVW6TrnuUHRSbK2vOfFpoXPXBjn3Sxvw',
#     'missing': ''
# }
#
# a = token_err.items()
#
# print(a.key)
# b = 1

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

b = fibonacci(10)

# 使用生成器
for num in fibonacci(10):
    print(num)
    pass


# g = (x*x for x in range(10))
# print(g)
# # print(next(g))
# # print(next(g))
#
# for i in list(g):
#     print(i)



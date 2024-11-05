# 1. 给你两个 非空 的链表， 便是两个非负的整数。 它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字0之外， 这两个数都不会以0开头
# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
# 输出: [7, 0, 8]

l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1.reverse()
l2.reverse()

i = 0
j = 0
str1 = ''
str2 = ''
while i < len(l1):
    # str1 = str1 + str(l1[i])
    str1 = str1 + str(l1[i])
    i = i + 1
while j < len(l2):
    str2 = str2 + str(l2[j])
    j = j + 1

num1 = int(str1)
num2 = int(str2)
num3 = num1 + num2  # int 类型的807

l3 = list(str(num3))
l3.reverse()
print(l3)

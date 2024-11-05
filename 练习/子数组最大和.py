import math

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_num = a[0]
curr_max_num = a[0]

# for i in len(a):
#     max_num = math.Max(a[i], curr_max_num+a[i+1])
#     curr_max_num = math.Max(max_num, curr_max_num)
#
# print(max_num)
i = 0

while i < len(a):

    curr_max_num = a[i] if a[i] > curr_max_num + a[i] else curr_max_num + a[i]
    max_num = max_num if max_num > curr_max_num else curr_max_num

    i = i + 1

print(max_num)


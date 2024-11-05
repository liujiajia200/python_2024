# 为抵抗洪水，战士连续作战89小时，编程计算共多少天零多少小时？
hour_work = 89
day = 89 // 24
hour = 89 % 24

print(f"战士作战了{day}天零{hour}小时")

from datetime import date

now = date.today()
print(now)

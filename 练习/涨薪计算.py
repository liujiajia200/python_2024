# 入职薪水10K，每年涨幅入职薪水的5%，50年后工资多少
import random


# money_base = 10000
#
# i = 1
# while i <= 50:
#     money_base = money_base * (1 + 0.05)
#     i = i + 1
#
# print(f"50年后的薪资是：{money_base}")

def generate_random_number(min, max, digit):
    """ Generate a given numerical digit random number, the numerical value range from min to max.

    :param min: the min number of the numerical value range (int)
    :param max: the max number of the numerical value range (int)
    :param digit: numerical digit of the generated number (int)
    :return: generate number (str)
    """

    return str(''.join(str(i) for i in random.sample(range(min, max), digit)))


a = random.choice(('E', 'F')) + generate_random_number(0, 9, 8)
print(a)

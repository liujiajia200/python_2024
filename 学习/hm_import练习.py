# 2. 导入.py文件中的某个模块
from hm_print不换行 import SayYes

SayYes().say_yes()  # 注意：SayYes是一个class，所以要加括号

# 3. 从别的文件夹中导入
from 练习 import 两数之和 as add

add  # 注意：add是整个文件，不用加括号


# 1. 直接导入
import hm_print不换行 as hn

hn.say_hello()




# from 练习 import 两数之和 as good
#
# good.lian_xu()
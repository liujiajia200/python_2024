# import time
#
# t = time.gmtime()
# print(t)
# tt = time.strftime("%Y-%M-%d", t)
# tt = time.strftime("%Y-%m-%d", t)
# print(tt)
#
# t_t = time.time()
# print(t_t)


# a = '123'
#
# print(a[0:30])
#
# print(float(13558))

class A:
    def __init__(self):
        self.logger = 'a'

class B(A):
    def __init__(self):
        super().__init__()

class C(B):
    def __init__(self):
        super().__init__()

c = C()
print(self.logger)

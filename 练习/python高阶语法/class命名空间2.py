a = 1


class C:
    a = 2

    def f(self):
        print(a)  # 1
        print(self.a)  # 2


c = C()
c.f()

l1 = [1, 2, 3]
l2 = [4, 5, 6]
d = l1 + l2
print(d)

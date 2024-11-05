a = 1


class C:
    print(a)
    a = 2
    print(a)

    class D:
        print(a)  # 1, 类和函数的最大差别之处：嵌套作用域在函数代码块里有用，在类中是没用的， 类D中没有变量a，它不会去找类C的a， 直接就去找全局变量中的a = 1

    x = [i ** a for i in range(5)]  # 个人理解：这行代码属于class C, 所以a取class C中的a变量
    print(x)

    @staticmethod
    def sm():
        print(a)  # C.sm()打印的是1，仅仅是调用了一个print()方法
        #  a = 1

    @classmethod
    def cm(cls):
        print(cls.a)  # print(C.a), cls表示本类, 因为在类C里，定义了属性a=2，即C.a = 2， 所以cls.a = 2

    def m(self):
        print(a)

    def m2(self):
        a = 3
        print(a)


C.sm()  # 1， 打印的外层的a, 等价于print(a)， 类里没定义，直接去全局变量找  # 个人理解 静态方法访问静态属性
C.cm()  # 2, 等价于 C.a
print(C.a)

c = C()
print(c.a)  # 2 c的属性值a初始定义为2
c.a = 123
print(c.a)  # 123 对象c的a属性修改为123
print(C.a)  # 2 整个类的属性值不变

print(c.m())
print(c.m2())

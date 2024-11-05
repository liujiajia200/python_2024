def add(a, b, *args):
    result = a + b
    for i in args:
        result += i
    print(result)


numbers = [1, 2, 3, 4]
add(*numbers)

a, b, c, d = numbers
add(a, b, c, d)

print('------------------------------')


def f1(a, b, *args):
    # 最正确写法
    print(a, b, args)


def f2(a, *args, b):
    # 合法但不推荐
    print(a, args, b)


def f3(a, *args, b=1):
    # 可以接受
    print(a, args, b)


def f4(a=1, *args, b=1):
    # 也不推荐
    print(a, args, b)


f1(1, 2, 3)
f2(1, 2, b=3)  # 如果不指定b=3就会报错
f3(1, 2, 3)
f4(1, 2, 3)
print('------------------------------')


def ff1(a, b=1, **kwargs):
    print(a, b, kwargs)


def ff2(a, *args, b=1, **kwargs):
    print(a, b, args, kwargs)


def ff3(*args, **kwargs):
    print(args, kwargs)


ff1(1, 2, x=3)  # 1 2 {'x': 3}
ff2(1, 2, 3)  # 1 1 (2, 3) {}
# f3(1, b=2, c=3)

d = {'a': 1, 'b': 2, 'c': 3}  # () {'a': 1, 'b': 2, 'c': 3}
ff3(**d)


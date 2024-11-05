from pprint import pprint as pp

a = 1
pp({'local:': locals(), 'globals:': globals()})


def f():
    a = 2
    print(a)
    pp({'local:': locals(), 'globals:': globals()})


class C:
    a = 3
    print(a)
    pp({pp({'local:': locals(), 'globals:': globals()})})


f()

# def f3():
#     print(a)
#     a = 3
#     print(a)
# f3()
a = 1

def f4():
    global a
    a = 4
    print(a)


f4()
print(a)

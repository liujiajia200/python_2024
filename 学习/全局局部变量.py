num = 10

def demo1():
    num =99
    print("demo1==>%d" %num)

def demo2():
    print("demo2==>%d" %num)


def demo3():
    global num  # 局部变量被改成100了
    num = 100
    print("demo3=>>%d" %num)

demo1()
demo2()
demo3()
print(num) # 输出100，因为再demo3中局部变量被改为100了


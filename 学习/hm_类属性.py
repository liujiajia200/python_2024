class Tool(object):
    count = 0

    def __init__(self, name):

        self.name = name

        Tool.count += 1


tool1 = Tool("哈哈哈")
tool2 = Tool("榔头")
tool3 = Tool("铁球")

print("工具实例个数是：%s" % Tool.count)
print(f"工具实例个数是：{Tool.count}")

# 通过对象名.类属性的方式访问类属性，本方法不推荐，
# 如果使用 对象.类属性 = 值 复制语句， 只会给对象添加一个属性， 而不会影响到类属性的值
# 因为只相当于给对象增加了一个属性，如果改变值，并不能改变类属性值

print("工具实例个数是：%s" % tool3.count)



# 调用方式 类名.方法名
# 在类方法内部： 可以通过cls.调用类属性和其他类方法

# 在类方法内部调用类属性和类方法是使用cls.方法名（属性）
# 在类外面调用类方法和类属性时使用 类名.方法名


class Tool(object):
    # 类属性
    count = 0

    # 类方法
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("猫咪")
tool2 = Tool("小兔子")
tool3 = Tool("狗熊")

Tool.show_tool_count()

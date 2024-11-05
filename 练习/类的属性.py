# class Bird(object):
#     feather = True  # 能继承
#
#     def __init__(self, num_leg):
#         self.num_leg = num_leg
#         self.att_bird = False
#
#
# class Chicken(Bird):
#     fly = False
#
#     def __init__(self, age, num_leg):
#         super().__init__(num_leg)
#         self.age = age
#
#
# summer = Chicken(2, 3)
# print(summer.att_bird)
# print(summer.num_leg)
# print(summer.feather)
# print(summer.age)

# print(Bird.__dict__)

class num(object):
    def __init__(self, value):
        self.value = value

    def getNeg(self):
        return -self.value

    def setNeg(self, value):
        self.value = -value

    def delNeg(self):
        print("value also deleted")
        del self.value

    neg = property(getNeg, setNeg, delNeg, "I'm negative")


c = num(3)

print(c.neg)

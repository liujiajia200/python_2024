name = ""
class Cat:

    def eat(self):
        print("%s爱吃鱼" % self.name)

tom = Cat()
tom.name = "Tom"
tom.eat()

lazy_cat=Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
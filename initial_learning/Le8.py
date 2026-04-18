class Point:
    def __init__(self, x, y):
          self.x = x
          self.y = y
        
    def move():
            print("move")

point1 = Point(10, 20)
print(point1.x)


class Mammals:
    def walk(self):
        print("Walk")


class Cat(Mammals):         
    def nya(self):
        print("Nyaaa~")


class Dog(Mammals):
    pass


cat1 = Cat()
cat1.nya()
dog1 = Dog()
dog1.walk()

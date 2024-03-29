class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        print("{}: I like {}!".format(self.name, food))

class Kitten(Animal):
    def make_sound(self):
        print("{}: Meow!".format(self.name))

class Puppy(Animal):
    def make_sound(self):
        print("{}: Woof!".format(self.name))

animals = [Kitten("Micka"), Puppy("Azor")]

for animal in animals:
    animal.make_sound()
    animal.eat("meat")

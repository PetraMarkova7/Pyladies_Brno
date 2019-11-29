class Dog:
    def __init__(self,name):
        self.name = name
        self.lives = 9
        self.bark()

    def __str__(self):
        return self.name

    def bark(self):
        print("haf", self.name)
    
    def eat(self, food):
        print(self.name, "eats", food)

if False:
    dog1 = Dog("tom")
    dog2 = Dog("john")

    dog1.bark()
    dog2.bark()

    dog1.eat("parek")
    dog1.eat("sunka")
    dog2.eat("sunka")
    print(dog2)


class Kitten:
    def __init__(self, name):
        self.name = name
        self.lives = 9

    def meow(self):
        print("meow", self.name)

    def is_alive(self):
        return self.lives > 0

    def lose_live(self):
        if self.is_alive():
            self.lives -= 1

    def add_live(self):
        if self.is_alive()and self.lives < 9:
            self.lives += 1

    def eat(self, food):
        if self.lives:
            if food == "fish":
                self.add_live()
                print("kocke pribudol zivot") 
            elif food == "poison":
                self.lose_live()
                print("vrahu")
            else:
                print("kocka papa")
        else:
            print("is dead")

micka = Kitten("micka")
print(micka.lives)
micka.eat("poison")
micka.eat("poison")
print(micka.lives)
micka.eat("fish")
print(micka.lives)




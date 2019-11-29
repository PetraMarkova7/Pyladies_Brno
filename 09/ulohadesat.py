class Politician:
    def __init__(self,name):
        self.name = name

    def drink(self, alco):
        print("{}: He likes {}!".format(self.name, alco))   

class Liar(Politician):
    def party(self):
        print("{}: Za Vlasť!".format(self.name))

class Thief(Politician):
    def party(self):
        print("{}: Za Smer".format(self.name))

    def drink(self, alco):
        print("{}: looks at {}!".format(self.name, alco))
        super().drink(alco)

class Brainless(Politician):  
    def party(self):
        print("{}: Za SNS".format(self.name))

class Nocomment(Politician):
    def __init__(self, name):
        name = name.replace("b", "t")
        super().__init__(name) 


harabin = Liar("Harabin")
fico = Thief("Fico") 
danko = Brainless("Danko")
harabin.drink("borovička")
harabin.party()
fico.party()
danko.party()
fico.drink("whiskey")
danko.drink("vodka")
kotleba = Nocomment("Kotleba")
kotleba.drink("slivovica")
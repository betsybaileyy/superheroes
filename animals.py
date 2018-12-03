class Tiger(object):
    """a tiger has a name, age, fav food"""
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.favorite_food = "catnip"

    def __str__(self):
        return "{} is {} years old".format(self.name, self.age)

    def eat(self, food):
        # print(self.name + " eats " + food)
        print("{} eats {}".format(self.name, food))
        if food == self.favorite_food:
            print("YUM, more " + food + " pls")

tony = Tiger("Tony", 66)
print(tony.name)
print(tony.name + " is " + str(tony.age) + " years old")
print("{} is {} years old".format(tony.name, tony.age)) #BEst practice for string formatting
tony.favorite_food = "Frosted Flakes™"
print("{}'s favorite food is {}".format(tony.name, tony.favorite_food))

hobbes = Tiger("Hobbes")
hobbes.age = 24
print("{} is {} years old".format(hobbes.name, hobbes.age))
print(hobbes)
hobbes.eat("fish")

tony.eat(tony.favorite_food)

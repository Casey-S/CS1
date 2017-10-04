# Implement the Animal superclass here
class Animal(object):
    population = 0

    def __init__(self, name):
        Animal.population += 1
        self.name = name

    @classmethod
    def populationCount(cls):
        return population

    def sleep(self):
        print("%s sleeps for 8 hours" % self.name)

    def eat(self, food):
        print("%s eats %s" % (self.name, food))
        if food == self.favoriteFood:
            print("YUM! %s wants more %s" % (self.name, food))


# Implement the Tiger class here as a subclass of Animal
# Hint: Implement the initializer method only
class Tiger(Animal):
    # Implement the initializer method here
    def __init__(self, name):
        super(Tiger, self).__init__(name)
        self.name = name
        self.favoriteFood = "meat"


# Implement the Bear class and its initializer, sleep and eat methods here
class Bear(Animal):
    # Implement the initializer method here
    def __init__(self, name):
        super(Bear, self).__init__(name)
        self.name = name
        self.favoriteFood = "fish"

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print("%s hibernates for 4 months" % self.name)


# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        super(Unicorn, self).__init__(name)
        self.name = name
        self.favoriteFood = "marshmallows"

    def sleep(self):
        print("%s sleeps in a cloud" % self.name)

# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
        super(Giraffe, self).__init__(name)
        self.name = name
        self.favoriteFood = "leaves"

    def eat(self, food):
        print("%s eats %s" % (self.name, food))
        if food == self.favoriteFood:
            print("YUM! %s wants more %s" % (self.name, food))
        else:
            print("YUCK! %s spits out %s" % (self.name, food))


# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
        super(Bee, self).__init__(name)
        self.name = name
        self.favoriteFood = "pollen"

    def eat(self, food):
        print("%s eats %s" % (self.name, food))
        if food == self.favoriteFood:
            print("YUM! %s wants more %s" % (self.name, food))
        else:
            print("YUCK! %s spits out %s" % (self.name, food))

    def sleep(self):
        print("%s never sleeps" % self.name)


# Implement the Zookeeper class here
class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Implement the feedAnimals method here
    def feedAnimals(self, animals, food):
        print("%s is feeding %s to %i of %i total animals" % (self.name, food, len(animals), Animal.population))
        for animal in animals:
            animal.eat(food)
            animal.sleep()

#Name :Ethan Mbila
#Date :23/02/2026
#inheritance

class Animal:
    def __init__(self, species, weight, food):
        self.species = species
        self.weight = weight
        self.food = food
    def grow(self, weight):
        weight = 1.1 * weight
        print(f"The animal weighs {weight}kg")
    def eat(self, food):
        print(f"The animal eats {food}")

class Dog(Animal):
    def __init__(self, colour, height, breed):
        super().__init__(species, weight, food)
        self.colour = colour
        self.height = height
        self.breed = breed
    def barks(self):
        print("The dog woofs")

class Horse(Animal):
    def __init__(self, species, weight, food):
        self.species = species
        self.weight = weight
        self.food = food
    def neighs(self):
        print("The horse neighs")
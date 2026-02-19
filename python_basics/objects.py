#Name :Ethan Mbila
#Date :19/02/2026
#CLasses(objects)

class Human:
    #attributes
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "ba sing se"
    #constructor
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age
    
    def tell_story(self):
        print(f"Hello, I am {self.human_name}. Here is a story")
        print("A loaf of bread, a container of bread and a Joe Dirt DVD")

#create the humans
don1 = Human("don1", 21)
don2 = Human("don2", 27)

#created humann to do things
don1.tell_story()
print("don1's age is", don1.human_age)

#modify one object
don1.city = "za"

print("don1's location:", don1.city)
print("don2's location:", don2.city)
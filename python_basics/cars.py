#Name :Ethan Mbila
#Date :23/02/2026
#classes

class Car:
    def __init__(self, model, make, colour, year):
        self.model = model
        self.make = make
        self.colour = colour
        self.year = year
    
    def print_details(self, model, make, colour, year):
        print(f"A {year} {make} {model} colour {colour}")
        
car1 = Car("E34", "BMW", "black", 1989)
car2 = Car("Camry", "Toyota", "grey", 2014)

car1.print_details("E34", "BMW", "black", 1989)
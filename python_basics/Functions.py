#Name :Ethan Mbila
#Date :19/02/2026
#Functions

def cook_egg():
    oil = "20ml"
    pan = True
    fire = True
    eggs = 2
    print(f"The pan is {pan}, and the fire is {fire}, add {oil} amount of oil and cook {eggs} eggs")

print("statement1")
print("statement2")    
cook_egg()
print("statement3")  

def fare(route, distance, rush_hour):
    fare = distance * 10
    if rush_hour == True:
        fare = fare * 1.5
    print(f"Yo fare to {route} is {fare}")
    return fare
rush_hour = True
returned_fare = fare("Juja-Allsops", 7, rush_hour)
print(f"The fare returned is {returned_fare}")

#passing a list as a parameter
def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interest}")
        
all_interests = ["political and economic state of the world😭✌🏾", "MUSIC"]
write_all_interests(all_interests)
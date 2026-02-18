#Name :Ethan Mbila
#Date :17/02/2026
#Output formatting

name = "don"
weight = 67 #kg
height = 195 #cm
tt = "Redbull"

#format using print(f"{}")
print(f"My name is {name} and I weigh {weight} kg")

#using fstring
msg = f"My name is {name} and I support {tt}"
print(msg)

#using {} and .format()
print("My name is {0} and I'm {1}cm tall".format(name, height))

#using %
print("I support %s" %tt)
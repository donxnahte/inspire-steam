#Name :Ethan Mbila
#Date :13/02/2026
#using for loop, print sin,cos,tan of numbers from -180 to +180 in steps of 30

import math
for x in range(-180, +180, 30):
    y = math.radians(x)
    print(f"Sine of {x} = {math.sin(y)}")
for x in range(-180, +180, 30):
    y = math.radians(x)
    print(f"Cosine of {x} = {math.cos(y)}")
for x in range(-180, +180, 30):
    y = math.radians(x)
    print(f"Tangent of {x} = {math.tan(y)}")

print("______________________________________________")
print(f"Angle {x}")
print("______________________________________________")
print(f"Cos {y}")
print("______________________________________________")
print(f"Angle {y}")
print("______________________________________________")
    
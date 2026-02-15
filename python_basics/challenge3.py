#Name :Ethan Mbila
#Date :13/02/2026
#using for loop, print sin,cos,tan of numbers from -180 to +180 in steps of 30

import math
for x in range(-180, +180, 30):
    x = math.radians(x)
    print(math.sin(x))
for x in range(-180, +180, 30):
    x = math.radians(x)
    print(math.cos(x))
for x in range(-180, +180, 30):
    x = math.radians(x)
    print(math.tan(x))
    
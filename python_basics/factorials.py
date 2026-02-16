#Name :Ethan Mbila
#Date :16/02/2026
#program to calculate factorials

num1 = int(input("Enter a number: "))
factorial = 1
for x in range(1, (num1 + 1)):
    factorial *= x
print(f"{num1}! = {factorial}")

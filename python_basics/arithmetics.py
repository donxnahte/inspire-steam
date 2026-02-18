#Name :Ethan Mbila
#Date :17/02/2026
#arithmetic operations

num1 = 12
num2 = 34
sum = num1 + num2
difference = num2 - num1
product = num1 * num2
quotient = num2 / num1

print("The sum of the numbers is %d" %sum)
print("The difference of the numbers is %d" %difference)
print("The quotient of the numbers is %f" %quotient)
print("The product of the numbers is %d" %product)

#modulus(%) - remainder
print(7 % 5)

#even and odd numbers
for x in range(0,21):
    y = x % 2
    if y == 0:
        print(f"{x} is even")
    elif y == 1:
        print(f"{x} is odd")
    
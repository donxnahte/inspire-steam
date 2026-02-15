#Name :Ethan Mbila
#Date :13/02/2026
#geometric progression

a = int(input("Enter the first number: "))
r = int(input("Enter the common ratio: "))
n = int(input("Enter the number of terms: "))

n_term = (a * r) ** (n - 1)
print("The nth term is", n_term)

if r > 1:
    sn = (a * ((r ** n) - 1)) / (r - 1)
elif r < 1:
    sn = (a * (1 - (r ** n))) / (1 - r)
else:
    sn = a * n

print("The sum of terms is", sn)
#Name :Ethan Mbila
#Date :13/02/2026
#Arithmetic progressions

#calculate the nth term
a = int(input("Enter first number: "))
n = int(input("Enter number of terms: "))
d = int(input("Enter the common difference: "))

n_term = a + ((n - 1)*d)
print("The nth term is", n_term)

sn = (n / 2)*((2*a) + ((n-1)*d))
print("The sum of the numbers is", sn)
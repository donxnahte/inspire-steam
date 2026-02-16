#Name :Ethan Mbila
#Date :16/02/2026
#calculate income tax : <50k - 2.5% , 50k-100k - 4.5%, >100k - 7.5%

salary = int(input("Enter yo gross salary: "))

if salary < 50000:
    tax = 0.025 * salary
    net_salary = salary - tax
elif salary > 50000 and salary < 100000:
    tax = 0.045 * salary
    net_salary = salary - tax
else:
    tax = 0.075 * salary
    net_salary = salary - tax
    
print(f"Gross salary = {salary}")
print(f"Tax = {tax}")
print(f"Net salary = {net_salary}")

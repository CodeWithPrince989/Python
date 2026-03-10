salary =int(input("Enter Your Salary:"))

if salary < 30000:
    print(salary*5/100)

elif 30000 <salary > 70000:
    print(salary*15/100)

elif salary > 70000:
    print(salary*25/100)

else:
    print("Enter Value is Not Salary")
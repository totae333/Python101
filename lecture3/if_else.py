num_employees = int(input("enter the number of employees: "))
if num_employees < 50:
    print("this is a small company")
elif num_employees < 250:
    print("this is a medium company")
elif num_employees >= 50:
    print("this is a large company")
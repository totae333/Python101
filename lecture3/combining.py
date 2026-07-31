age = int(input("age:"))
income = int(input("income:"))

if age >= 18 and age <= 65 and income > 30000:
    print("you are eligible for the loan")
else:
    print("you are not eligible for the loan")
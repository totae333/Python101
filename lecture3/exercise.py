hour_worked = int(input("number of hour worked:"))
pay_rate = int(input("hourly pay rate:"))

if hour_worked > 40:
    (pay_rate*1.5)* hour_worked

gross_pay = (hour_worked * pay_rate)

print("gross pay is:", gross_pay)
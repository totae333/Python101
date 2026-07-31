#for i in range(5):
#    print(i)

#for i in range(3,10):
#   print(i)

#for i in range(1,11,2):
#    print(i)

print('number\tsquare')
print('--------------')

for number in range(1,11):
    square = number**2
    print(number, "\t", square)

print('kph\tmph')
print('--------------')

for kph in range(60,130,10):
    mph = kph*0.6214
    print(kph, "\t", mph)
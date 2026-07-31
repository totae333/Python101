#numbers = [6,5,3,8,4,2,5,4,11]

#sum = 0
#for val in numbers:
#    sum += val
#    print(sum)

#print('the sum is', sum)

max = int(input('enter max:'))

total = 0.0

print('ths program is calculate the sum of')
print(max, 'number u will enter')

for counter in range(max):
    nimber = int(input('enter nember:'))
    total = total + nimber
print("the total is", total)
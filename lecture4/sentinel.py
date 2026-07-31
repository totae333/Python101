keep_going = 'y'

while keep_going == 'y':
    sale = float(input('enter cost of sales: '))
   # retail = float(input('enter the retail price: '))
    retail = sale * 2.5
    print(f'the retail is ${retail:.2f}')
    keep_going = input('do u want to calculate another'+ 'retail (enter y for yes): ')
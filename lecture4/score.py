score =     int(input('enter a tesst score: '))
while score < 0 or score > 100:
    print('error score can not be negative')
    print('or greater than 100')
    score = int(input('enter correct score: '))
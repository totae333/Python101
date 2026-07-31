inchar = input("input one character:")
if inchar >= 'A' and inchar <= 'Z':
    print("you input upper letter", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("you input lower letter", inchar)
elif inchar >= '0' and inchar <= '9':
    print("you input upper letter", inchar)
else:
    print("it not a letter or number", inchar)
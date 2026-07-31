row = int(input("enter row:"))

for i in range(1,101):
    print(i, end=" ")
    if i % row == 0:
        print()
    
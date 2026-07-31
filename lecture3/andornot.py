#x = 10
#y = 20
#z = 30

#if x < y and y < z:
#    print("x less than y and y less than z")
#if x < y or y > z:
#    print("either x less than y or y is greater than z")
#if not (x > y):
#    print("x is not greater than y")


a = [1, 2, 3]
b = a

c = [1, 2, 3]
d = [1, 2, 3]

print(a is b)
print(a is c)
print(c is d)

print(a == c)
print(c == d)
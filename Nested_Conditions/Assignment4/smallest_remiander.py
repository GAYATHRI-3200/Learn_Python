a = int(input())
b = int(input())

c = (a % b)
d = (b % a)
if ( c <= d ):
    print(c)
else:
    print(d)

a=int(input())
b=int(input())
c=int(input())

if (a<b or a<c and a==b and a==c):
    print(a)
elif(b<c or b<a and b==c):
    print(b)
else:
    print(c)
    
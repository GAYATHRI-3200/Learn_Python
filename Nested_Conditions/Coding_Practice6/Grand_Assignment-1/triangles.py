a=int(input())
b=int(input())
c=int(input())
C1 = a==b==c
C2 =  (a==b or b==c or a==c)

if a==b==c:
    print("Equilateral")
elif C2:
    print("Isosceles")
else:
    print("Scalene")
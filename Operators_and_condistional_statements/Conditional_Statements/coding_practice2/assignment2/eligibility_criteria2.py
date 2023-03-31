M=int(input())
P=int(input())
C=int(input())
sum= (M + P + C)
a= (M + P)
b = ( M + C)
c = ( P + C )
if (a >= 100 or b >= 100 or c >= 100 ) and (sum >= 180):
    print("True")
else:
    print("False")
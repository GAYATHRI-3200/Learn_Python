M=int(input())
P=int(input())
C=int(input())
sum= (M + P + C)
a= (M + P)
b = ( M + C)
c = ( P + C )
if ( M >= 35 and P >= 35 and C >= 35) and (a >=90 or b >= 90 or c >= 90 ):
    print("True")
else:
    print("False")
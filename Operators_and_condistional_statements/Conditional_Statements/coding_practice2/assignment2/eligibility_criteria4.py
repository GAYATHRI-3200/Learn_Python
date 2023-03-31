M=int(input())
P=int(input())
C=int(input())
sum= (M + P + C)
a= (M + P)
b = ( M + C)
c = ( P + C )
if ( M >= 60 or P >= 50 or C >= 45) and (sum >= 180) or (a >= 120 or  c >= 110 ):
    print("True")
else:
    print("False")
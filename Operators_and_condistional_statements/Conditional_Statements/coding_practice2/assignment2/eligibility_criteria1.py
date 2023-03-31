M=int(input())
P=int(input())
C=int(input())
sum = ( M + P + C)
if (M >= 70 and P >= 60 and C >= 60) or ( sum >= 180):
    print("True")
else:
    print("False")
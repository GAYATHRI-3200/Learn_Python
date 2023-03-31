n = int(input())
rem = (n%11)

c1 = (rem==0)
c2 = (rem==1)

if (c1 or c2):
    print("Special Eleven")
else:
    print("Normal Number")
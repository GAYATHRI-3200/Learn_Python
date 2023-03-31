num=input()

a1 = int(num[0])
a2 = int(num[1])
rem= int(num) % 9
c1 = (a1 == 9 or a2 == 9)
c2 = (rem == 0)

if (c1 or c2 ):
    print("Lucky Number")
else:
    print("Unlucky Number")
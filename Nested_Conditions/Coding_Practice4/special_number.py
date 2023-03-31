num=input()
a1 = int(num[0])
a2 = int(num[1])
add = int(a1 + a2)

rem= int(num) % 7

c1 = (add == 7)
c2 = (a1 == 7 or a2 == 7)
c3 = (rem == 0)

if (c1 or c2 or  c3):
    print("Special Number")
else:
    print("Normal Number")
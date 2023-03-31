n = input()
l = len(n)
a = 0
for i in n:
    a = a +(int(i) ** l)
if a == int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
a = int(input())
b = int(input())

n1 = a ** b
n2 = b ** a
if n1 > n2:
    print(n1)
else:
    print(n2)
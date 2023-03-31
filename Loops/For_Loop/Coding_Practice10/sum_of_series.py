n = int(input())
repeat = "2"
total = 0
for i in range(1, n+1):
    R = repeat * i
    total = total + int(R)
print(total)
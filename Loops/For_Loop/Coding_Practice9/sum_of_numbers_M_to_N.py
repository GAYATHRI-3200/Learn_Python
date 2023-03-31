M = int(input())
N = int(input())
sum = 0
for i in range(M, N+1):
    sum = sum+i
    i += 1
print(sum)
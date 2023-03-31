M = int(input())
N = int(input())
product = 1
for i in range(M, N+1):
    product  = product * i
    i += 1
print(product )
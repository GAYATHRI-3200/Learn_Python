a = [2,1,5,6,4,3,8,7,9]
tg = 10
#[[3,7],[1,9],[2,8],....]

res1 = []

for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i] + a[j] == tg:
            res1.append((a[i],a[j]))
print(res1)

#ouput: [[2, 8], [1, 9], [5, 5], [6, 4], [3, 7]]

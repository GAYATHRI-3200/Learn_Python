num = input()

l= len(num)
n1 = int(num[0])
n2 = int(num[l-2]) 
n3 = int(num[l-1]) 

add = (n1 ** l) + (n2 ** l) + (n3 ** l)
res = int(num) == int(add)

if res:
    print("True")
else:
    print("False")
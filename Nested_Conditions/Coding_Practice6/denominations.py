amt = int(input())
n_100 = 0
n_50 = 0
n_10 = 0
n_1 = 0
if amt >= 100:
    n_100 = int(amt/100)
    amt = (amt % 100)
if amt >= 50:
    n_50 = int(amt/50)
    amt = (amt % 50)
if amt >= 10:
    n_10 = int(amt/10)
    amt = (amt % 10)
n_1 = amt
print("100:"+str(n_100))
print("50:"+str(n_50))
print("10:"+str(n_10))
print("1:"+str(n_1))
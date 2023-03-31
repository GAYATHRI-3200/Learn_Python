amt = int(input())
n_100 = 0
n_50 = 0
n_20 = 0
n_10 = 0
if amt >= 100:
    n_100 = int(amt/100)
    amt = (amt % 100)
if amt >= 50:
    n_50 = int(amt/50)
    amt = (amt % 50)
if amt >= 20:
    n_20 = int(amt/20)
    amt = (amt % 20)
if amt >= 10:
    n_10 = int(amt/10)
    amt = (amt % 10)
n_1 = amt
print("100 Notes: "+str(n_100))
print("50 Notes: "+str(n_50))
print("20 Notes: "+str(n_20))
print("10 Notes: "+str(n_10))
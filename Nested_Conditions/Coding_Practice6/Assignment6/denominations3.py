amt = int(input())
n_500 = 0
n_50 = 0
n_10 = 0
n_1 = 0
if amt >= 500:
    n_500 = int(amt/500)
    amt = (amt % 500)
if amt >= 50:
    n_50 = int(amt/50)
    amt = (amt % 50)
if amt >= 10:
    n_10 = int(amt/10)
    amt = (amt % 10)
n_1 = amt
print("500: "+str(n_500) + " 50: " + str(n_50) + " 10: " + str(n_10)  + " 1: " + str(n_1))

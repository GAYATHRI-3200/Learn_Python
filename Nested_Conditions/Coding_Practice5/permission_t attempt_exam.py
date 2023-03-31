n = input()
x = input()

y = (int(n[0:-1]) >= (75))

if y:
    print("Allowed to write exam")
elif x == "Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")
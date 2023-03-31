D = input()
N = int(input())
if D == "Sunday":
    d = 0
if D == "Monday":
    d = 1
if D == "Tuesday":
    d = 2
if D == "Wednesday":
    d = 3
if D == "Thursday":
    d = 4
if D == "Friday":
    d = 5
if D == "Saturday":
    d = 6
day = d + (N-1)
day = day % 7
if day == 0:
    d = "Sunday"
    print(d)
if day == 1:
    d = "Monday"
    print(d)
if day == 2:
    d = "Tuesday"
    print(d)
if day == 3:
    d = "Wednesday"
    print(d)
if day == 4:
    d = "Thursday"
    print(d)
if day == 5:
    d = "Friday"
    print(d)
if day == 6:
    d = "Saturday"
    print(d)

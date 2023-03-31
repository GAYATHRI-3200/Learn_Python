n = int(input())
Year = int(n/365)

remaining_days = int(n-(Year)*365)
Weeks = int(remaining_days/7)
Days = int(remaining_days-(Weeks)*7)
print(Year)
print(Weeks)
print(Days)

n = int(input())

Winter = ( n == 1 or n == 11 or n == 12 )
Spring = ( n == 2 or n == 3 )
Summer = ( n == 4 or n == 5 or n == 6 )
Rainy = ( n == 7 or n == 8 )
Autumn = ( n == 9 or n == 10 )

if Winter:
    season = "Winter"
elif Spring:
    season = "Spring"
elif Summer:
    season = "Summer"  
elif Rainy:
    season = "Rainy"
else:
    season = "Autumn"
print(season)
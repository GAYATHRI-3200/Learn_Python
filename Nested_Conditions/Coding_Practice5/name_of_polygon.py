s = int(input())

if ( s < 3 ):
    print("Not Polygon")
elif ( s == 3 ):
    print("Triangle")
elif ( s == 4 ):
    print("Quadrilateral")
elif ( s == 5 ):
    print("Pentagon")
else:
    print("Big Polygon")
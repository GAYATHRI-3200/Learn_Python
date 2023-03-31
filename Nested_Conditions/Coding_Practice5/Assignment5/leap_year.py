input_year = int(input())

if (input_year%400 == 0):
    print("True")
elif (input_year%100 == 0):
    print("False")
elif (input_year%4 == 0):
    print("True")
else:
    print("False")

    
a=int(input())

if a%6==0:
    print("Number is divisible by 6")

if a%3==0 and a%6!=0:
    print("Number is divisible by 3")

if a%2==0 and a%6!=0:
    print("Number is divisible by 2")

if a%2 != 0 and a%3 != 0:
    print("Number is not divisible by 2, 3 or 6")
    

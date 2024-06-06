#Check whether a string is palindrome or not

def check_palindrome(s):
    return s == s[::-1]

s = "MOM"
if check_palindrome(s):
    print("Yes it is palindrome")
else:
    print("No")
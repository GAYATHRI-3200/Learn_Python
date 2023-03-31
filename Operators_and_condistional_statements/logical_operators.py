"""Logical Operators
The logical operators are used to perform logical operations on Boolean values.
Gives True or False
Operators are and,or,not"""

n1 = int(input())#integer type(5)
n2 = int(input())#integer type (10)
print(n1 < n2 and n1 > n2) #False
print(n1 < n2 or n1 > n2) #True
print(not(n1)) #False
print(not(n2)) #False

s1 = input() #string type #True
s2 = input() #string type #False
print(s1 and s2) #False
print(s1 or s2) #True
print(not(s1)) #False
print(not(s2)) #False
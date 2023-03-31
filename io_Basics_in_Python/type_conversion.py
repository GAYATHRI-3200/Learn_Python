"""String Slicing:
Obtaining a part of a string is called string slicing

Checking Data Type:
Check the datatype of the variable or value using type() 

Type Conversion:
Converting the value of one data type to another data type is called Type Conversion or Type Casting.


1. String to Integer
int() converts valid data of any type to integer
2. Integer to Float
str() converts data of any type to a string.
3. Float to String
float() Converts to float data type"""
a = input()#123456 # Reads a line of input as a string.
#print(a)
print(a[0:])#String Slicing at start
print(a[:4])#String Slicing at end

print(type(a)) #str()
to_int = int(a)
print(to_int)
print(type(to_int)) #int()
to_float = float(a)
print(to_float)
print(type(to_float))

"""I/P: 123456
O/P:
123456
1234
<class 'str'>
123456
<class 'int'>
123456.0
<class 'float'>"""

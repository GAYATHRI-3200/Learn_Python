"""Inputs and Outputs Basics:
input():
Allows flexibility to take the input from the user.Reads a line of input as a string.

String Concatenation:
Joining strings together is called string concatenation.

String Repetition:
* operator is used for repeating strings any number of times as required.

Length of String:
len() returns the number of characters in a given string.

String Indexing:
We can access an individual character in a string using their positions (which start from 0) .
These positions are also called as index."""

Name = input() # Reads a line of input as a string.
print(Name)

str_concat = Name + Name
print(str_concat) #String Concatenation

str_repeat = Name * 2
print(str_repeat) #String Repetition

Length = len(Name)
print(Length) #Length of String

str_index = [Name[0]]
print(str_index) #String Indexing

"""
I/P: 
gayathri
O/P:
gayathri
gayathrigayathri
gayathrigayathri
8
['g']
"""
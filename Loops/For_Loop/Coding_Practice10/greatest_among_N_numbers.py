number_of_inputs = int(input())

first_input = int(input())
l_number = first_input

for i in range(number_of_inputs - 1):
    number = int(input())
    if number > l_number:
        l_number = number

print(l_number)
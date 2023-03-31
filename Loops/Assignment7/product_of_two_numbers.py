number_of_inputs = int(input())

counter = 0
product = 1
while counter < number_of_inputs:
  number = int(input())
  product = product * number
  counter = (counter + 1)
print(product)
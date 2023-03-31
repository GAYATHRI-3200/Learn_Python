word = input()
index = int(input())
skip = word[:index] + word[index+1:]
print(skip)
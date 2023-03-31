word = input()
l = len(word)
stars = "*" * (l-4)
print(word[0:2] + stars + word[l-2:])
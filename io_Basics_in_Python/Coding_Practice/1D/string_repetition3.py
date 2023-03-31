W = input()
N = int(input())
l = len(W)
last3_char = W[l-3:]
str_repeat = last3_char * N
print(str_repeat)
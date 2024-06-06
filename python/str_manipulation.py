#String manipulation: "The Sky is Blue" to "Blue is The Sky"

s = "The Sky is Blue"
l = s.split()
l = l[::-1]
l = ' '.join(l)
print(l)

#remove punctuation, except space
a ="/@The Sky is Blue"
s = ''
for i in a:
    if ((i >= 'A' and i<='Z') | (i>='a' and i<='z') | (i== ' ')):
        s = s+i
print(s)
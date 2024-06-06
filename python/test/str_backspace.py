# S, T = "cb#c", "ad#c"
S, T = "ab##", "c#d#"
def str_backspace(S):
    l = []
    for i in S:
        if i == '#':
            print(i)
            if l:
                l.pop()
        else:
            l.append(i)
    print(l)
    return ''.join(l)

def str_task(S,T):
    return str_backspace(S) == str_backspace(T)

print(str_task(S,T))
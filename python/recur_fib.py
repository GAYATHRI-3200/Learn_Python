#Create a Fibonacci series using recursion

def recur_fib(n):
    if n<=1:
        return n
    else:
        return recur_fib(n-1) + recur_fib(n-2)
    
n = 10
for i in range(n):
    print(recur_fib(i))
#1. Generate an infinite Fibonacci series using a generator
def infinite_fib():
    a,b = 0,1
    while True:
        yield a
        a, b =  b, a+b

fib_series = infinite_fib()
for _ in range(10):
    print(next(fib_series))
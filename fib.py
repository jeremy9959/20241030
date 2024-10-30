def fib(n):
    f, fx = 0, 1
    for i in range(n):
        f, fx = fx, f+fx
    return f


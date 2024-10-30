def fib(n):
    "Returns the nth fibonacci number."
    f, fx = 0, 1
    for i in range(n):
        f, fx = fx, f+fx
    return f


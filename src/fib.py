def fib(n):
    "Returns the nth fibonacci number."
    f, fx = 0, 1
    for i in range(n):
        f, fx = fx, f+fx
    return f

if __name__ == "__main__":
    n = input("What n do you want? ")
    print(f"{n}th Fibonacci number is: {fib(int(n))}")
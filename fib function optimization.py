def fib(n):
    if n == 0 or n == 1:
        return n
    x = fib(n - 1)
    y = fib(n - 2)
    return x + y


print(fib(10))

# 1,1,2

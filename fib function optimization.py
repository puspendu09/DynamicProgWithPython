# memoization
# key=> fib(n) value=>return value
# to implement this we need dictionary in python;


def fib(n, memo={}):
    if n in memo.keys():
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        # print(memo)
        return memo[n]


# print('fib(n)', fib(2))
print('fib(n)', fib(7))
# print('fib(n)', fib(4))
# print('fib(n)', fib(50))


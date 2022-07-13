

def gridTraveler(m, n, memo={}):

    # memo checking
    # are the args in the memo
    key = str(m) + ',' + str(n)
    if key in memo.keys():
        return memo[key]

    # base case
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    # recursion of function actual call of the  function
    memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[key]



print(gridTraveler(1, 1))
print(gridTraveler(2, 3))
print(gridTraveler(0, 1))
print(gridTraveler(59, 16))  # 77558760

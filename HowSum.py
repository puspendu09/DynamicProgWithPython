# write a function 'howSum(targetSum, numbers)' that takes in  a targetSum
# and an array of numbers as  argument
#
# the function should return an array containing any combination of element that add up to exactly
# the targetSum. if there is no combination that adds up tp the targetSum then return null;

# if there are multiple combination possible, you may return any single one.

# howSum(7, [5, 3, 4, 7]) --->[3, 4]
# howSum(7, [2, 4]) ---> null


def howSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remainder = targetSum - num
        remainder_result = howSum(remainder, numbers, memo)
        # print(remainder_result)
        if remainder_result is not None:
            memo[targetSum] = (*remainder_result, num)
            print(targetSum)
            return memo[targetSum]

    memo[targetSum] = None
    return None


print(howSum(7, [5, 3, 4, 7]))
print(howSum(3, [2, 1, 7]))
# print(howSum(3, [2, 7]))
print(howSum(300, [3, 7, 5, 10]))


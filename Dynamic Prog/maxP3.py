def maxP3(input_numbers):
    sorted_numbers = sorted(input_numbers)
    # print(sorted_numbers)
    hi3 = sorted_numbers[-1] * sorted_numbers[-2] * sorted_numbers[-3]
    # print(hi3)
    lo2hi1 = sorted_numbers[0] * sorted_numbers[1] * sorted_numbers[-1]
    # print(lo2hi1)
    return max(hi3, lo2hi1)


numbers1 = [-1, 3, 5, 7, 0]
numbers2 = [-3, -5, 5, 7, 0]

numbers3 = [-8, 3, 5, 7, 0]

print(maxP3(numbers1))
print(maxP3(numbers2))
print(maxP3(numbers3))

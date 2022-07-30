def binary_search(sorted_input, target, start, end):
    # if end >= start:
    #     mid = int((start + end) // 2)
    #     # print(id(sorted_input))
    #     # print(sorted_input[mid])
    #     if sorted_input[mid] == target:
    #         return mid
    #     elif sorted_input[mid] > target:
    #         # end = mid - 1
    #         return binary_search(sorted_input, target, start, mid - 1)
    #     else:
    #         start = mid + 1
    #         return binary_search(sorted_input, target, mid + 1, end)
    # else:
    #     return
    ########################################################################
    while start <= end:
        if target > sorted_input[len(sorted_input) - 1]:
            return -1
        # print("start-", start, "end-", end)
        mid = int((start + end) / 2)
        # print("mid-", mid, ",value at mid-", sorted_input[mid], ",target-", target)
        if sorted_input[mid] == target:
            return mid
        elif sorted_input[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    # print("start value after while loop-", start)
    return sorted_input[start]


sorted_input_test = [0, 1, 2, 4, 5, 7, 9, 12]
print(binary_search(sorted_input_test, 18, 0, len(sorted_input_test) - 1))

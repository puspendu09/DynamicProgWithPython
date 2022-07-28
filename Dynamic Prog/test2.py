def binary_search(sorted_input, target, start, end):
    if end >= start:
        mid = int((start + end) // 2)
        print(id(sorted_input))
        # print(sorted_input[mid])
        if sorted_input[mid] == target:
            return mid
        elif sorted_input[mid] > target:
            # end = mid - 1
            return binary_search(sorted_input, target, start, mid - 1)
        else:
            start = mid + 1
            return binary_search(sorted_input, target, mid + 1, end)
    else:
        return -1
    ########################################################################
    # while start <= end:
    #     mid = int((start + end) / 2)
    #     if sorted_input[mid] == target:
    #         return mid
    #     elif mid > target:
    #         end = mid - 1
    #     else:
    #         start = mid + 1
    #
    # return -1


sorted_input_test = [1, 2, 3, 4, 5, 10,12,13,14,15,16]
print(binary_search(sorted_input_test, 12, 0, len(sorted_input_test) - 1))

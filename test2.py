def binary_search(numbers, start: int, end: int, target_value):
    if start > end:
        return -1
    mid = int((start + end) / 2)

    if numbers[mid] == target_value:
        return mid
    if target_value < numbers[mid]:
        return binary_search(numbers, start, mid - 1, target_value)

    return binary_search(numbers, mid + 1, end, target_value)


number_array = [-1, 2, 3, 4, 5, 6, ]
print(binary_search(number_array, 0, len(number_array) - 1, -5))

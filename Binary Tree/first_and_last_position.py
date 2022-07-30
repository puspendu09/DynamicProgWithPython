def binary_search(nums, target):
    start = 0
    end = len(nums) - 1
    ans = [-1, -1]
    while start <= end:
        mid = int((start + end) / 2)
        if nums[mid] == target:  # found potential ans
            # start_position(nums, start)
            first_value = start_position(nums, target, True)
            end_value = start_position(nums, target, False)
            ans[0] = first_value
            ans[1] = end_value

        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return ans


def start_position(nums, target, findStartIndex):
    start = 0
    end = len(nums) - 1
    ans = -1
    while start <= end:
        mid = int((start + end) / 2)
        # if nums[mid] == target:  # found potential ans

        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            ans = mid
            if findStartIndex:
                end = mid - 1
            else:
                start = mid + 1

    return ans


numbers = [1, 2, 4, 7, 7, 7, 7, 8]
print(binary_search(numbers, 7))

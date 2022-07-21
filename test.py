def binarySearch(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        if list[mid] > left:
            left = mid + 1
        else:
            right = mid - 1
    return None


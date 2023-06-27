from typing import List, Optional


def binary_search(arr: List[int or float], target: Optional[int, float]) -> Optional[int]:
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1


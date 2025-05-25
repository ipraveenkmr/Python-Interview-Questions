#  Example 1: Linear Search

def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False

# Best case (Ω): When the target is at index 0 → Ω(1)
# Worst case (O): Target is at the end or not present → O(n)

#  Example 2: Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Best case: Array is already sorted — still goes through loops, but no swaps
# Optimized versions skip inner loop if no swaps, giving Ω(n)
# Worst case: Reversed array → many swaps → O(n²)


#  Example 3: Binary Search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


# Best case: Target is at the middle on the first try → Ω(1)
# Worst case: Requires log₂(n) steps → O(log n)
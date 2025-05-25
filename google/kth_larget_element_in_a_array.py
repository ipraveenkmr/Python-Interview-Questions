# Program 1
# import heapq

# def find_kth_largest(nums, k):
#     return heapq.nlargest(k, nums)[-1]

# Output
# print(find_kth_largest([3,2,1,5,6,4], 2)) 

# heapq.nlargest(k, nums) is efficient for small k, and better than sorting the whole list.
# Internally, it uses a min-heap of size k, so its time complexity is:
# O(n log k) — more efficient than full sort (O(n log n)) when k is small.


# Program 2
def find_kth_largest(nums, k):
    return sorted(nums, reverse=True)[k - 1]

# Efficient: O(n log k)
# Good for very large lists and small k

# Output
print(find_kth_largest([3,2,1,5,6,4], 2))  # 5



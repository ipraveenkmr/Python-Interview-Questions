from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    return [x for x, _ in freq.most_common(k)]

# Output
print(top_k_frequent([1,1,1,2,2,3], 2))  # [1, 2]

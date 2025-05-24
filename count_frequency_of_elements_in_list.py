from collections import Counter


def count_frequency(lst):
    return dict(Counter(lst))


# Example
print(count_frequency(["a", "b", "a", "c", "b"]))
# Output: {'a': 2, 'b': 2, 'c': 1}

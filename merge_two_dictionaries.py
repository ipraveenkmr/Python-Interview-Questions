# Method 1: Python 3.9+
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Method 2: For older Python
merged = {**dict1, **dict2}

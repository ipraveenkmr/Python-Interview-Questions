def longest_unique_substring(s):
    char_index = {}
    start = max_len = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_len = max(max_len, i - start + 1)

    return max_len

# Example
print(longest_unique_substring("abcabcbb"))  # Output: 3

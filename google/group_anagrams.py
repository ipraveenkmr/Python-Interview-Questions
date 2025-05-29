from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        key = tuple(sorted(word))
        print('key ', key)
        anagrams[key].append(word)
    return list(anagrams.values())

# Output
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

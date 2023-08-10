from collections import defaultdict

def group_anagrams(strs):
    anagram_groups = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    
    return list(anagram_groups.values())

input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(input_strings)
print(result)

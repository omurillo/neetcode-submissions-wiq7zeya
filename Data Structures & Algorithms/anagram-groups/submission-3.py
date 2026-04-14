from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        result = []
        for word in strs:
            sorted_word = tuple(sorted(word))
            dictionary[sorted_word].append(word)

        return list(dictionary.values())

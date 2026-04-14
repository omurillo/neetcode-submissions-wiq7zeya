from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        word_set = defaultdict(list)
        for word in strs:
                word_sorted = tuple(sorted(word))
                word_set[word_sorted].append(word)
        return list(word_set.values())
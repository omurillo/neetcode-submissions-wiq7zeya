from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        res_array = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            result[sorted_word].append(word)
        for value in result.values():
            res_array.append(value)
        return res_array


        
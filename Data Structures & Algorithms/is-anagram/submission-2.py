from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = defaultdict(int) , defaultdict(int)

        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1
        for key in count_s.keys():
            if count_s.get(key) != count_t.get(key):
                return False
        return True
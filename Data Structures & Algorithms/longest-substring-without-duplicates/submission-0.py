class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        maxLength = 0
        right = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in res:
               res.add(s[right])
               maxLength = max(maxLength, right - left + 1)
            else :
                while s[left] != s[right]:
                    res.remove(s[left])
                    left += 1
                left += 1
        return maxLength
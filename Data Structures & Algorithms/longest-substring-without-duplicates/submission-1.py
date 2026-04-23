class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = set()
        max_len = 0
        right = left = 0
        for right in range(len(s)):
            while s[right] in duplicates:
                duplicates.remove(s[left])
                left += 1
            max_len = max(max_len, right - left + 1)
            duplicates.add(s[right])
        return max_len
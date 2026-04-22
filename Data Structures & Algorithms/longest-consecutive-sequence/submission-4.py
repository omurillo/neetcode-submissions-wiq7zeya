class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1
        
        num_set = set(nums)
        max_longest = 0
        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                max_longest = max(max_longest, length)
        return max_longest


                

            

from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = defaultdict(int)
        for i in range(len(nums)):
            res = target - nums[i]
            if res in total:
                return [total[res], i]
            total[nums[i]] = i
        
        
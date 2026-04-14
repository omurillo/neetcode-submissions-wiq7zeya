from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in total:
                return [total[diff], i]
            else:
                total[nums[i]] = i
        
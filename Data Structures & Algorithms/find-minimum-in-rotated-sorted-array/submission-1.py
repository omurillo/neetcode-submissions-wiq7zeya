class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minVal = float('inf')
        while left <= right:
            middle = left + ((right - left)//2)
            if nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] < nums[left]:
                right = middle - 1
            else:
                minVal = min(minVal, nums[middle])
                break    
            minVal = min(minVal, nums[middle])
        minVal = min(minVal, nums[left])
        return minVal
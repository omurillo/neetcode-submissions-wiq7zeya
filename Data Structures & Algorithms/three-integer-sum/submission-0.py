class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        result = []

        for i in range (len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left,right = i + 1, len(nums) - 1
            target = nums[i]
            while left < right:
                threeSum = target + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([target, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1

        return result
                
                    

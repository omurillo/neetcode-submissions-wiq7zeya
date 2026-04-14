class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(speed):
            return sum((pile + speed - 1) // speed for pile in piles) <= h
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if not possible(mid):
                left = mid + 1
            else:
                right = mid
        return left
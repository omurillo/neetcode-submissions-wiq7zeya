class Solution:
    def fillStack(self, filler: List[int], heights: List[int], stack: List[int], i: int):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            filler[i] = stack[-1]
        stack.append(i)
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftMost = [-1] * n
        for i in range(n):
            self.fillStack(leftMost, heights, stack, i)

        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            self.fillStack(rightMost, heights, stack, i)
        
        maxArea = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
        return maxArea
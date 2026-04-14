class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = deque([("", 0, 0)])
        result = []
        while queue:
            current, left, right = queue.popleft()
            if left == n and right == n:
                result.append(current)
            if left < n:
                queue.append([current + "(", left + 1, right])
            if right < left:
                queue.append([current + ")", left, right + 1])
        return result



        

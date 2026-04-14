class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            False
        for row in matrix:
            if row[len(row) - 1] < target:
                continue
            elif row[0] > target:
                return False
            left = 0
            right = len(row) - 1
            while left <= right:
                middle = left + ((right - left) // 2)
                if row[middle] > target:
                    right = middle - 1
                elif row[middle] < target:
                    left = middle + 1
                else:
                    return True
        return False

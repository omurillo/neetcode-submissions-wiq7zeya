class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        subgrid_set = [[set() for _ in range(3)] for _ in range(3)]
        
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in row_set[row]:
                    return False
                if num in col_set[col]:
                    return False
                if num in subgrid_set[row // 3][col // 3]:
                    return False
                row_set[row].add(num)
                col_set[col].add(num)
                subgrid_set[row // 3][col//3].add(num)
        return True
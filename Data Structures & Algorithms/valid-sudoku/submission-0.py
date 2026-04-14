class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_row(board: List[List[str]]) -> bool:
            for row in board:
                if not is_valid(row):
                    return False
            return True

        def is_valid_col(board: List[List[str]]) -> bool:
            for col in range(9):
                column = [board[row][col] for row in range(9)]
                if not is_valid(column):
                    return False
            return True

        def is_valid_square(board: List[List[str]]) -> bool:
            for row in range(0, 9, 3):
                for col in range(0, 9, 3):
                    square = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
                    if not is_valid(square):
                        return False
            return True

        def is_valid(values: List[str]) -> bool:
            seen = set()
            for value in values:
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
            return True

        return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)
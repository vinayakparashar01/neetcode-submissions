class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for row in board:
            seen.clear()
            for i in row:
                if i == ".":
                    continue
                if i in seen :
                    return False
                seen.add(i)
        for c in range(9):
            seen.clear()
            for r in range(9):
                if board[r][c]==".":
                    continue
                if board[r][c] in seen :
                    return False
                seen.add(board[r][c]) 
        seen.clear()        
        for st_r in range(0, 9, 3):
            for st_c in range(0, 9, 3):
                seen = set()
                for j in range(3):
                    for k in range(3):
                        value = board[st_r + j][st_c + k]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)
        return True

        
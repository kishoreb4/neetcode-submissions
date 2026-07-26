class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for each_row in board:
            each_row = [x for x in each_row if x != '.' and x.isnumeric()]
            if (len(each_row) != len(set(each_row))):
                return False
        for i in range(len(board)):
            each_col = [row[i] for row in board]
            each_col = [x for x in each_col if x != '.' and x.isnumeric()]
            if (len(each_col) != len(set(each_col))):
                return False
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                box = [board[i+r][j+c] for r in range(3) for c in range(3)]
                box = [x for x in box if x != '.' and x.isnumeric()]
                if len(box) != len(set(box)):
                    return False
        return True   
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            li = [x for x in row if x.isdigit()]
            if len(set(li)) != len(li):
                return False
        for i in range(0,len(board)):    
            li = [x[i] for x in board if x[i].isdigit()]
            if len(set(li)) != len(li):
                return False
        
         # Validate 3x3 boxes
        for box_row in range(0, len(board), 3):
            for box_col in range(0, len(board), 3):
                li = [board[r][c] for r in range(box_row, box_row + 3) 
                      for c in range(box_col, box_col + 3) if board[r][c].isdigit()]
                if len(set(li)) != len(li):
                    return False
            
 
        return True   
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        while i < len(board):
            if len(set([x for x in board[i] if x !='.'])) != len([x for x in board[i] if x !='.']):
                print(f"i={i}")
                return False
            else:
                i+=1
        j = 0        
        while j < len(board):
            if len(set([row[j] for row in board if row[j]!='.'])) != len([row[j] for row in board if row[j]!='.']):
                print(f"j={j}")
                return False
            else:
                j+=1
                
        # k = 0 
        for box_row in range(0,3):
            for box_col in range(0,3):
                box = []
                for i in range(box_row * 3, box_row * 3 + 3):
                    for j in range(box_col * 3, box_col * 3 + 3):
                        if board[i][j] != '.':
                            box.append(board[i][j])
                if len(set(box)) != len(box):
                    return False
        return True   
        
        
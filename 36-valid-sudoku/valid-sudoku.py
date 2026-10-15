class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Time Complexity = O(n^2)
        # space Complexity = O(n^2)
        
        row = [set() for i in range(9)]
        column = [set() for i in range(9)]
        box = [set() for i in range(9)]

        for i in range(81):
            r = i // 9
            c = i % 9
            box_index = (r//3) * 3 + c//3 
            
            val = board[r][c]
            if val == '.':
                continue
            
            if val in row[r] or val in column[c] or val in box[box_index]:
                return False
            
            row[r].add(val)
            column[c].add(val)
            box[box_index].add(val)

        return True
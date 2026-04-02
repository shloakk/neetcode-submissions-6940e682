import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        hm_rows = dict.fromkeys(digits)
        hm_columns = dict.fromkeys(digits)
        hm_boxes = dict.fromkeys(["11", "12", "13", "21", "22", "23", "31", "32", "33"])

        for key in hm_rows:
            hm_rows[key] = []
        for key in hm_columns:
            hm_columns[key] = []
        for key in hm_boxes:
            hm_boxes[key] = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                x = math.ceil((i+1)/3)
                y = math.ceil((j+1)/3)

                print(val)
                print(hm_rows[1])
                if val in hm_rows[i+1] or val in hm_columns[j+1] or val in hm_boxes[str(x)+str(y)]:
                    print(hm_rows)
                    print(hm_columns)
                    print(hm_boxes)
                    return False
                
                hm_rows[i+1] += [val]
                hm_columns[j+1] += [val]
                hm_boxes[str(x)+str(y)] += [val]
        
        return True
                
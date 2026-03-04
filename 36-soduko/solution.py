from typing import List, Set

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_dict = {0: set(),
                    1: set(),
                    2: set(),
                    3: set(),
                    4: set(),
                    5: set(),
                    6: set(),
                    7: set(),
                    8: set()}
        column_dict = {0: set(),
                    1: set(),
                    2: set(),
                    3: set(),
                    4: set(),
                    5: set(),
                    6: set(),
                    7: set(),
                    8: set()}
        row_temp = set()
        for j in range(9): #rows
            row_temp.clear()
            for i in range(9): #columns
                if "." in board[j][i]:
                    continue
                if board[j][i] in row_temp:
                    print(f"In row {j}")
                    return False
                else:
                    if board[j][i] in column_dict[i]:
                        print(f"In column {i}")
                        return False
                    else:
                        
                        column_dict[i].add(board[j][i])
                        row_temp.add(board[j][i])
                        sub_box_key = (j//3) * 3 + (i//3)
                         
                        if board[j][i] in box_dict[sub_box_key]:
                           
                            return False
                        else:
                            box_dict[sub_box_key].add(board[j][i])
        return True 
                        

                
        

def main():
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    sol = Solution()
    result = sol.isValidSudoku(board)
    print(result)


if __name__ == "__main__":
    main()
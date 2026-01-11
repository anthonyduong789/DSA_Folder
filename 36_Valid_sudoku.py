class Solution(object):
    def isValidSuoku(self, board):
        """
        track digits and check horizontal 
        vertical boxes if valid use hash to check if ther are repeats
        we know that the boxes are 0-2 / 0-2 vertically| 3-5 / 0-2 | 6-8 / 0-2
        """
        boxCheck = []
        #now we need to check vertically we will do it by place in the
        verticalChecks = [{} for _ in range(9)]
        for row in range(len(9)):
            # checks horizontally for suoku valid
            rowCheck = {}
            for col in range(len(9)):
                # this will check horizontally for matches
                if board[row][col] == ".": 
                    pass
                elif board[row][col] in rowCheck:
                    return False
                else
                    rowCheck[board[row][col]] == 1


if __name__ == "__main__":
    print(bfs_find(matrix, start, target_value))
             



    




            
                





            
        
        

        

        

















